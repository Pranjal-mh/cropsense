import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from .disease_data import DISEASE_INFO, get_disease_info
from .ml_service import PredictionError, classify_image
from .models import DetectionRecord
from .serializers import (
    DetectionRecordSerializer,
    DetectionResponseSerializer,
    ImageUploadSerializer,
)

logger = logging.getLogger(__name__)


def index(request):
    """Simple demo page with an upload form that calls the API via JS."""
    return render(request, "detector/index.html")


class HealthCheckView(APIView):
    """GET /api/health/ - simple uptime/config check."""

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "model": settings.HF_MODEL_ID,
                "inference_mode": settings.HF_INFERENCE_MODE,
            }
        )


class DiseaseListView(APIView):
    """GET /api/diseases/ - list every disease class the model can detect."""

    def get(self, request):
        return Response(
            [
                {"label": label, **info}
                for label, info in DISEASE_INFO.items()
            ]
        )


class DetectDiseaseView(APIView):
    """
    POST /api/detect/  (multipart/form-data, field name: "image")

    Runs the uploaded leaf photo through the Hugging Face model and
    returns the predicted crop, disease, confidence, and a remedy.
    """

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_file = serializer.validated_data["image"]
        image_bytes = image_file.read()

        try:
            raw_predictions = classify_image(image_bytes)
        except PredictionError as exc:
            logger.warning("Prediction failed: %s", exc)
            return Response(
                {"error": str(exc)}, status=status.HTTP_502_BAD_GATEWAY
            )

        if not raw_predictions:
            return Response(
                {"error": "The model returned no predictions for this image."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        enriched = []
        for pred in raw_predictions[:5]:
            info = get_disease_info(pred["label"])
            enriched.append({**info, "confidence": round(float(pred["score"]), 4)})

        best = enriched[0]

        # Save to history (best-effort; don't fail the request if this errors)
        try:
            image_file.seek(0)
            DetectionRecord.objects.create(
                image=image_file,
                crop=best["crop"],
                disease=best["disease"],
                raw_label=best["label"],
                confidence=best["confidence"],
                is_healthy=best["is_healthy"],
                remedy=best["remedy"],
            )
        except Exception:
            logger.exception("Could not save detection record")

        payload = {
            "prediction": best,
            "alternatives": enriched[1:],
            "model": settings.HF_MODEL_ID,
        }
        out = DetectionResponseSerializer(payload)
        return Response(out.data, status=status.HTTP_200_OK)


class DetectionHistoryView(ListAPIView):
    """GET /api/history/ - most recent detections, newest first."""

    queryset = DetectionRecord.objects.all()[:50]
    serializer_class = DetectionRecordSerializer
