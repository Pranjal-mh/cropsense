from django.urls import path

from . import views

app_name = "detector"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/health/", views.HealthCheckView.as_view(), name="health"),
    path("api/diseases/", views.DiseaseListView.as_view(), name="diseases"),
    path("api/detect/", views.DetectDiseaseView.as_view(), name="detect"),
    path("api/history/", views.DetectionHistoryView.as_view(), name="history"),
]
