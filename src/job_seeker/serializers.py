from rest_framework import serializers

from src.job_seeker.models import Job_Seeker, Skill


class Job_SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Seeker
        fields = ['user', 'education', 'experience', 'phone']


class SeekerSkillSerializer(serializers.ModelSerializer):
    model = Skill
    fields = ['skill', 'job_seeker']
