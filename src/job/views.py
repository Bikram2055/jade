import datetime

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.permissions import IsEmployer
from src.job.models import Job
from src.job.serializers import CategorywiseJobSerializer, JobSerializer

# from src.users.models import User

# Create your views here.


class JobApi(generics.ListCreateAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]


class JobUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]


class Number_Of_JObs(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request):
        """
        Return a list of all users.
        """
        no_of_jobs = Job.objects.all().count()
        return Response({"Jobs count": no_of_jobs})


class Job_Count_Category(APIView):
    def get(self, request):

        data = Job.objects.values('category__category').annotate(count=Count('id'))
        serializer = CategorywiseJobSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer = serializer
        return Response(serializer.data)


class JobAge(APIView):
    def get(self, request, id):

        today = datetime.date.today()
        job_post_date = get_object_or_404(Job, id=id)
        if job_post_date is not None:
            age = -(datetime.datetime.date(job_post_date.created_at) - today).days
            return Response({'age': age})
        return Response(status=status.HTTP_404_NOT_FOUND)
