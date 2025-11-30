from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    department = models.CharField(max_length=50)



# Create your models here.
