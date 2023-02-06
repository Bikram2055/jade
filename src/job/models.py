from django.db import models

from src.employer.models import Employer
from src.users.models import TimeStampAbstractModel

# Create your models here.


class Job(TimeStampAbstractModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    budget = models.FloatField()
    duration = models.DurationField()
    requirement = models.FileField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


class Required_Skill(TimeStampAbstractModel):
    skill = models.CharField(max_length=30)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
