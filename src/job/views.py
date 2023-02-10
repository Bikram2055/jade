import datetime

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, status
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
    """This is a Python class that implements an API endpoint for getting the count of job posts in each category.
    The class is a subclass of APIView from the Django REST framework and defines a single method, get,
     which implements the endpoint.
    """

    def get(self, request):
        """api get method

        Args:
            request (object): used to get data from endpoint

        Returns:
            data(json): category wise job count
        """
        data = Job.objects.values('category__category').annotate(count=Count('id'))
        serializer = CategorywiseJobSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer = serializer
        return Response(serializer.data)


class JobAge(APIView):
    """This is a Python class that implements an API endpoint for getting the age of a job post in days.
    The class is a subclass of APIView from the Django REST framework and defines a single method, get,
     which implements the endpoint.
    """

    def get(self, request, id):
        """api get method

        Args:
            request (object): used to get data from endpoint
            id (int): job id

        Returns:
            age(int): age of job
        """

        today = datetime.date.today()
        job_post_date = get_object_or_404(Job, id=id)
        if job_post_date is not None:
            age = -(datetime.datetime.date(job_post_date.created_at) - today).days
            return Response({'age': age})
        return Response(status=status.HTTP_404_NOT_FOUND)


class SearchJob(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
