from django.urls import reverse
from django.shortcuts import redirect
from django.db import models
from customer.models import Customer
from account.models import Profile
from datetime import datetime

# Create your models here.

status = [
    ('Developing','Developing'),
    ('Requirment Gathering','Requirment Gathering'),
    ('Testing','Testing'),
    ('validating','Validating')
]

class Project(models.Model):
    project_name = models.CharField(max_length= 100)
    start_date = models.DateField(default = datetime.now())
    deploy_date = models.DateField(default = datetime.now())
    status = models.CharField(max_length= 50 ,choices = status , default= "Developing")
    amount = models.PositiveIntegerField(default= 0)
    paid_amount = models.PositiveIntegerField(default=0)
    remainig_work = models.CharField(max_length= 500, null=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="Customer_name")
    project_manager = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('project-list')


    def __str__(self):
        return f"{self.project_name}"