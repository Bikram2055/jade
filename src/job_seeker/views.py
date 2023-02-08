from rest_framework import generics, permissions

from src.job_seeker.models import Job_Seeker, Skill
from src.job_seeker.serializers import Job_SeekerSerializer, SeekerSkillSerializer

# from rest_framework.response import Response
# from rest_framework.views import APIView


# from src.users.models import User

# Create your views here.


class Seekers(generics.ListCreateAPIView):

    queryset = Job_Seeker.objects.all()
    serializer_class = Job_SeekerSerializer
    permission_classes = [permissions.AllowAny]


class SeekerUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Job_Seeker.objects.all()
    serializer_class = Job_SeekerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


class SeekerSkillUpdate(generics.RetrieveAPIView):

    queryset = Skill.objects.all()
    serializer_class = SeekerSkillSerializer


class SeekerSkill(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SeekerSkillSerializer
