from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from src.employer.models import Employer
from src.employer.serializers import EmployerSerializer

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
