from rest_framework import serializers

from src.employer.serializers import EmployernameSerializer
from src.job.models import Bid, Category, Job, Project, Rating, Required_Skill


class RequireskillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Required_Skill
        fields = ['skill']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class JobSerializer(serializers.ModelSerializer):

    skill = RequireskillSerializer(many=True)
    category_name = CategorySerializer(source='category')
    employer_data = EmployernameSerializer(source='employer')

    def create(self, validated_data):
        skills = validated_data.pop('skill')
        job = super().create(validated_data)
        for skill in skills:
            instance, created = Required_Skill.objects.get_or_create(skill=skill['skill'])
            job.skill.add(instance)
        return job

    def update(self, instance, validated_data):
        skills = validated_data.pop('skill')
        job = super().update(instance, validated_data)
        job.skill.clear()
        for skill in skills:
            instance, created = Required_Skill.objects.get_or_create(skill=skill['skill'])
            job.skill.add(instance)
        return job

    class Meta:
        model = Job
        fields = [
            'name',
            'description',
            'category_name',
            'budget',
            'duration',
            'requirement',
            'employer_data',
            'is_draft',
            'skill',
        ]


class CategorywiseJobSerializer(serializers.Serializer):

    category__category = serializers.CharField()
    count = serializers.IntegerField()


class BidperJobSerializer(serializers.Serializer):

    job__name = serializers.CharField()
    count = serializers.IntegerField()

    # class Meta:
    #     model = Bid
    #     fields = ['job', 'count']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['employer', 'job_seeker', 'job', 'rating', 'feedback']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['job', 'proposal', 'amount', 'job_seeker', 'require_days', 'milestone']


class JobnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name']


class ShortlistSerializer(serializers.ModelSerializer):
    project = JobnameSerializer(source='job')

    class Meta:
        model = Bid
        fields = ['project', 'job_seeker', 'is_shortlisted']
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Project
        fields = ['job', 'job_seeker', 'employer', 'is_active', 'is_finished']
