import io
from unittest.mock import patch

from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from .disease_data import get_disease_info
from .models import DetectionRecord


def make_test_image():
    buf = io.BytesIO()
    Image.new("RGB", (64, 64), color=(60, 120, 60)).save(buf, format="JPEG")
    buf.seek(0)
    buf.name = "leaf.jpg"
    return buf


class DiseaseDataTests(APITestCase):
    def test_known_label_lookup(self):
        info = get_disease_info("Tomato___Late_blight")
        self.assertEqual(info["crop"], "Tomato")
        self.assertFalse(info["is_healthy"])
        self.assertIn("fungicide", info["remedy"].lower() + info["remedy"])

    def test_unknown_label_falls_back_gracefully(self):
        info = get_disease_info("Mango___Some_new_disease")
        self.assertEqual(info["crop"], "Mango")
        self.assertFalse(info["is_healthy"])


class HealthCheckTests(APITestCase):
    def test_health_endpoint(self):
        response = self.client.get(reverse("detector:health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")


class DiseaseListTests(APITestCase):
    def test_lists_all_38_classes(self):
        response = self.client.get(reverse("detector:diseases"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 38)


class DetectDiseaseViewTests(APITestCase):
    @patch("detector.views.classify_image")
    def test_successful_detection_returns_remedy_and_saves_history(self, mock_classify):
        mock_classify.return_value = [
            {"label": "Tomato___Late_blight", "score": 0.92},
            {"label": "Tomato___Early_blight", "score": 0.05},
        ]

        response = self.client.post(
            reverse("detector:detect"),
            {"image": make_test_image()},
            format="multipart",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["prediction"]["disease"], "Late Blight")
        self.assertEqual(response.data["prediction"]["crop"], "Tomato")
        self.assertAlmostEqual(response.data["prediction"]["confidence"], 0.92)
        self.assertEqual(len(response.data["alternatives"]), 1)
        self.assertEqual(DetectionRecord.objects.count(), 1)

    def test_rejects_missing_image(self):
        response = self.client.post(reverse("detector:detect"), {}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rejects_non_image_file(self):
        bad_file = io.BytesIO(b"not an image")
        bad_file.name = "leaf.jpg"
        response = self.client.post(
            reverse("detector:detect"), {"image": bad_file}, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("detector.views.classify_image")
    def test_upstream_failure_returns_502(self, mock_classify):
        from .ml_service import PredictionError

        mock_classify.side_effect = PredictionError("Hugging Face API unavailable")
        response = self.client.post(
            reverse("detector:detect"),
            {"image": make_test_image()},
            format="multipart",
        )
        self.assertEqual(response.status_code, status.HTTP_502_BAD_GATEWAY)


class DetectionHistoryTests(APITestCase):
    def test_history_endpoint_returns_records(self):
        DetectionRecord.objects.create(
            image="uploads/test.jpg",
            crop="Tomato",
            disease="Late Blight",
            raw_label="Tomato___Late_blight",
            confidence=0.9,
            is_healthy=False,
            remedy="Apply fungicide.",
        )
        response = self.client.get(reverse("detector:history"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
