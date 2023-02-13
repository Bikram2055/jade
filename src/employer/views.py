from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.permissions import IsEmployer
from src.employer.models import Employer
from src.employer.serializers import EmployerSerializer
from src.job.models import Job, Rating
from src.job.serializers import JobSerializer, RateSerializer

# Create your views here.


class EmployerApi(generics.ListCreateAPIView):
    """This is a Django class-based view for handling the creation and retrieval of
    "Employer" objects. The view is using Django Rest Framework's generics.ListCreateAPIView class,
     which provides the ability to list and create instances of a model.
    """

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.AllowAny]


class EmployerUpdate(generics.RetrieveUpdateDestroyAPIView):
    """This is a Django class-based view for handling updates to an "Employer" model. The view is
    using Django Rest Framework's generics.RetrieveUpdateDestroyAPIView class, which provides the
     ability to retrieve, update, and delete a single instance of a model.
    """

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


class Number_Of_Employers(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request):
        """
        Return a list of all users.
        """
        no_of_employers = Employer.objects.all().count()
        return Response({"employers count": no_of_employers})


class RateApi(generics.ListCreateAPIView):

    queryset = Rating.objects.all()
    serializer_class = RateSerializer
    permission_classes = [
        IsEmployer,
    ]


class DraftJob(LoginRequiredMixin, generics.ListAPIView):

    queryset = Job.objects.filter(is_draft=True)
    serializer_class = JobSerializer
    permission_classes = [IsEmployer]
