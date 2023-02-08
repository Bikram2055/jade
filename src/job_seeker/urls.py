from django.urls import path

from src.job_seeker import views

urlpatterns = [
    path("", views.Seekers.as_view()),
    path("update/<int:pk>", views.SeekerUpdate.as_view()),
    path("skills/", views.SeekerSkill.as_view(), name="add-skills"),
    path("skill-update/<int:pk>", views.SeekerSkillUpdate.as_view(), name="update-skills"),
]
