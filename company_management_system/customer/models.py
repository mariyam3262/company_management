from django.db import models
from django.urls import reverse
# Create your models here.

class Customer(models.Model):
    owner_name = models.CharField(max_length= 30)
    company_name = models.CharField(max_length= 50)
    contact_number = models.CharField(max_length= 15)
    alt_contact_num = models.CharField(max_length= 15)
    address = models.CharField(max_length= 200)
    project_category = models.CharField(max_length= 100)
    project = models.CharField(max_length= 200)
    description = models.CharField(max_length= 500)
    requirement_pdf = models.FileField(upload_to = 'customer/images', null = True)
    reference = models.URLField(blank= True)


    def __str__(self):
        return f"{self.company_name} | {self.owner_name}"

    def get_absolute_url(self):
        return reverse('customer-list')
        


