from django.db import models

# Create your models here.
class employeeDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField()
    hired_date = models.DateField()
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
