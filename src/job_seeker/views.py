from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common import serializers
from src.users.models import User

# Create your views here.


class Seekers(APIView):
    def get(self, request):

        data = User.objects.all()
        serializer = serializers.UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
