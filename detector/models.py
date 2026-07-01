from django.db import models


class DetectionRecord(models.Model):
    """Stores each analyzed leaf image along with the model's prediction."""

    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    crop = models.CharField(max_length=100)
    disease = models.CharField(max_length=150)
    raw_label = models.CharField(max_length=150)
    confidence = models.FloatField(help_text="Model confidence score, 0-1")
    is_healthy = models.BooleanField(default=False)
    remedy = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.crop} - {self.disease} ({self.confidence:.2%})"
