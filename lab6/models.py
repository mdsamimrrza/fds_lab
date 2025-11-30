from django.db import models


class Placement(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
