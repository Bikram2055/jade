from rest_framework import generics, permissions

from src.common.permissions import IsEmployer
from src.job.models import Job
from src.job.serializers import JobSerializer

# from rest_framework.response import Response
# from rest_framework.views import APIView


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
