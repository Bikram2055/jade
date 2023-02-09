from rest_framework import serializers

from src.job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'description', 'category', 'budget', 'duration', 'requirement', 'employer', 'is_draft']


class CategorywiseJobSerializer(serializers.Serializer):

    category__category = serializers.CharField()
    count = serializers.IntegerField()
