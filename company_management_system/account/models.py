from django.shortcuts import redirect
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category = [
    ('Developer','Developer'),
    ('HR','HR'),
    ('Project Manager','Project Manager'),
    ('Marketing Person','Marketing Person')
]



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 50)
    designation = models.CharField(max_length= 50)
    join_date = models.DateField()
    dob = models.DateField()
    working_duration = models.CharField(max_length=20)
    rewards = models.CharField(max_length= 500)
    # category = models.CharField(max_length= 50, choices=category, default='Developer')

    def __str__(self):
        return f"{self.full_name}"

   