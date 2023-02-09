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
    """This is a class-based view in Django Rest Framework (DRF) using the RetrieveUpdateDestroyAPIView
     class from the generics module. It defines a view for updating a Job_Seeker instance.

    The queryset attribute specifies the queryset that the view will use to retrieve the Job_Seeker instance
     to be updated. It is set to Job_Seeker.objects.all(), meaning that the view will retrieve all Job_Seeker
      instances.

    The serializer_class attribute specifies the serializer that will be used to serialize and deserialize
     the data. In this case, it is set to Job_SeekerSerializer.

    The permission_classes attribute specifies the permissions that must be satisfied in order to access
     this view. In this case, it is set to [permissions.IsAuthenticatedOrReadOnly], meaning that either the
      user must be authenticated, or the request method must be a safe method such as GET (read-only).
    """

    queryset = Job_Seeker.objects.all()
    serializer_class = Job_SeekerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


class SeekerSkillUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Skill.objects.all()
    serializer_class = SeekerSkillSerializer


class SeekerSkill(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SeekerSkillSerializer
