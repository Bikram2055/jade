from django.urls import path

from src.employer import views

urlpatterns = [
    path("", views.Employer.as_view()),
]
