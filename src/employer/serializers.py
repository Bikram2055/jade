from rest_framework import serializers

from src.employer.models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['user', 'description', 'phone']
