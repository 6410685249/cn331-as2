from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(primary_key=True, max_length=6)
    professor = models.CharField(max_length=128)
    semester = models.IntegerField()
    year = models.CharField(max_length=4)
    quota = models.BooleanField(default=False)
    seat = models.IntegerField()