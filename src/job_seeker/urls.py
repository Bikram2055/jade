from django.urls import path

from src.job_seeker import views

urlpatterns = [
    path("", views.Seekers.as_view()),
]
