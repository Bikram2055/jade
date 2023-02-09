from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from src.employer.models import Employer
from src.employer.serializers import EmployerSerializer

# from rest_framework.response import Response
# from rest_framework.views import APIView


# from src.users.models import User

# Create your views here.


class EmployerApi(generics.ListCreateAPIView):

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.AllowAny]


class EmployerUpdate(generics.RetrieveUpdateDestroyAPIView):

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
