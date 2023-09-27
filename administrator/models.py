from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=6)
    professor = models.CharField(max_length=128)
    quota = models.BooleanField(default=False)
    seat = models.IntegerField()