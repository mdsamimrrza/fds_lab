from django.db import models

# Create your models here.
class examfeemodel(models.Model):
        name = models.CharField(max_length=100)
        usn = models.CharField(max_length=20)
        sem = models.IntegerField()
        exam_fee = models.IntegerField()
