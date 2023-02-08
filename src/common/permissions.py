from rest_framework import permissions

from src.employer.models import Employer


class IsEmployer(permissions.BasePermission):
    def has_permission(self, request, view):

        if Employer.objects.filter(user=request.user).exists():
            return True
        return False
