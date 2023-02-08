from django.urls import path

from src.employer import views

urlpatterns = [
    path("update/<int:pk>", views.EmployerUpdate.as_view()),
    path("", views.EmployerApi.as_view(), name="create-employer"),
]
