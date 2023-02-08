from django.db import models
from phone_field import PhoneField

from src.users.models import TimeStampAbstractModel, User

# Create your models here.


class Job_Seeker(TimeStampAbstractModel):

    rating = models.FloatField()
    education = models.CharField(max_length=250)
    experience = models.FloatField()
    phone = PhoneField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Skill(TimeStampAbstractModel):

    skill = models.CharField(max_length=30)
    job_seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)
