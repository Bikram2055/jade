from django.urls import path

from src.job import views

urlpatterns = [path("update/<int:pk>", views.JobUpdate.as_view()), path("", views.JobApi.as_view())]
