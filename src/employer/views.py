from rest_framework import generics, permissions

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
