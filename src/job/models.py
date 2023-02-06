from django.db import models

from src.employer.models import Employer
from src.job_seeker.models import Job_Seeker
from src.users.models import TimeStampAbstractModel

# Create your models here.


class Job(TimeStampAbstractModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    budget = models.FloatField()
    duration = models.DurationField()
    requirement = models.FileField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)


class Required_Skill(TimeStampAbstractModel):
    skill = models.CharField(max_length=30)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class Project(TimeStampAbstractModel):

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    is_finished = models.BooleanField()


class Bid(TimeStampAbstractModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    proposal = models.CharField(max_length=150)
    amount = models.FloatField()
    job_seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)
    require_days = models.IntegerField()
    milestone = models.CharField(max_length=300)
    is_shortlisted = models.BooleanField(default=False)
