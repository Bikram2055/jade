from django.urls import path

from src.job import views

urlpatterns = [
    path("update/<int:pk>", views.JobUpdate.as_view()),
    path("", views.JobApi.as_view()),
    path("no-of-jobs/", views.Number_Of_JObs.as_view()),
    path("categorywise-jobcount/", views.Job_Count_Category.as_view()),
    path("job-age/<int:id>", views.JobAge.as_view()),
    path("search/", views.SearchJob.as_view()),
]
