from rest_framework import serializers

from src.job.models import Bid, Job, Rating


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'description', 'category', 'budget', 'duration', 'requirement', 'employer', 'is_draft']


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
