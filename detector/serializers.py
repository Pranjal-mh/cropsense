from rest_framework import serializers

from .models import DetectionRecord


class ImageUploadSerializer(serializers.Serializer):
    """Validates the incoming multipart image upload."""

    image = serializers.ImageField()

    def validate_image(self, value):
        from django.conf import settings

        if value.size > settings.MAX_UPLOAD_SIZE:
            max_mb = settings.MAX_UPLOAD_SIZE / (1024 * 1024)
            raise serializers.ValidationError(f"Image must be smaller than {max_mb:.0f}MB.")
        return value


class PredictionResultSerializer(serializers.Serializer):
    """Shape of a single top-N prediction returned by the model."""

    label = serializers.CharField()
    crop = serializers.CharField()
    disease = serializers.CharField()
    is_healthy = serializers.BooleanField()
    confidence = serializers.FloatField()
    description = serializers.CharField()
    remedy = serializers.CharField()
    prevention = serializers.CharField()


class DetectionResponseSerializer(serializers.Serializer):
    """Top-level API response: best prediction + alternatives."""

    prediction = PredictionResultSerializer()
    alternatives = PredictionResultSerializer(many=True)
    model = serializers.CharField()


class DetectionRecordSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = DetectionRecord
        fields = [
            "id",
            "image_url",
            "crop",
            "disease",
            "raw_label",
            "confidence",
            "is_healthy",
            "remedy",
            "created_at",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if not obj.image:
            return None
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url
