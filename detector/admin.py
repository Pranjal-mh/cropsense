from django.contrib import admin

from .models import DetectionRecord


@admin.register(DetectionRecord)
class DetectionRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "crop", "disease", "confidence", "is_healthy", "created_at")
    list_filter = ("crop", "is_healthy")
    readonly_fields = [f.name for f in DetectionRecord._meta.fields]
