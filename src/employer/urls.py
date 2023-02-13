from django.urls import path

from src.employer import views

urlpatterns = [
    path("update/<int:pk>", views.EmployerUpdate.as_view()),
    path("", views.EmployerApi.as_view(), name="create-employer"),
    path("no-of-employers/", views.Number_Of_Employers.as_view()),
    path("rate/", views.RateApi.as_view()),
]
