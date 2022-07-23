from datetime import datetime
from django.db import models
from account.models import Profile
from project.models import Project
from django.urls import reverse

# Create your models here.

class Attendance(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    date = models.DateField(default = datetime.now())
    reporting_time = models.TimeField()
    total_attendance = models.IntegerField(default= 0)
    leaving_time = models.TimeField()

    def __str__(self):
        return f"{self.user}|{self.total_attendance}"
    
    def get_absolute_url(self):
        return reverse('attendance-list')



class DailyReport(models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    designation = models.CharField(max_length= 30, default='Developer')
    date = models.DateField(default= datetime.now())
    working_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    performedTask_today = models.CharField(max_length= 1000, blank=False)
    performedTask_next_day = models.CharField(max_length= 1000, blank=True)


    def get_absolute_url(self):
        return reverse('dailyReport-list')


    