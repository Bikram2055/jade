from django.db import models

from src.employer.models import Employer
from src.job_seeker.models import Job_Seeker
from src.users.models import TimeStampAbstractModel

# Create your models here.


class Job(TimeStampAbstractModel):
    '''This class for add jobs by employer'''

    name = models.CharField(max_length=30)
    '''CharField: for name of project'''
    description = models.CharField(max_length=250)
    '''CharField: for description of project'''
    budget = models.FloatField()
    '''FloatField: for define budget of project'''
    duration = models.DateField(null=True)
    '''DateField: for last date of project'''
    requirement = models.FileField()
    '''FileField: for file related to project'''
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    '''ForeginKey: for which employer add the project'''
    is_draft = models.BooleanField(default=False)
    '''BooleanField: for status of project to save as draft'''

    def __str__(self) -> str:
        return self.name


class Required_Skill(TimeStampAbstractModel):
    '''This class is for skills set required to fullfill specific project'''

    skill = models.CharField(max_length=30)
    '''CharField: for skill required for project'''
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    '''ForeignKey: for link specific jobs to required skills'''

    def __str__(self) -> str:
        return self.skill


class Project(TimeStampAbstractModel):
    '''This class for Project status'''

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    '''ForeignKey: for specific project status'''
    job_seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)
    '''ForeignKey: for specific employee who is doing such project'''
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    '''ForeignKey: for specific employer who add such project'''
    is_active = models.BooleanField()
    '''BooleanField: for status of project is active or not'''
    is_finished = models.BooleanField()
    '''BooleanField: for status of project is finished or not'''


class Bid(TimeStampAbstractModel):
    '''This class is for record of job_seekers who wants to do specific job'''

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    '''ForeignKey: for specific project'''
    proposal = models.CharField(max_length=150)
    '''CharField: for proposal given by job_seeker to project'''
    amount = models.FloatField()
    '''FloatField: for job_seeker biding amount'''
    job_seeker = models.ForeignKey(Job_Seeker, on_delete=models.CASCADE)
    '''ForeignKey: for specify job_seeker'''
    require_days = models.IntegerField()
    '''IntegerField: for number of days to complete the project assigned by job seeker'''
    milestone = models.CharField(max_length=300)
    '''CharField: for set milestone of project'''
    is_shortlisted = models.BooleanField(default=False)
    '''BooleanField: for status of shortlisted job seeker by employer'''
