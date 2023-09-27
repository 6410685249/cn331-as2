from django.db import models
# from administrator.models import Subject

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    id = models.CharField(primary_key=True, max_length=10)
    status = models.BooleanField(default=False)
    # subjects = models.ManyToManyField(Subject, blank=True, related_name="list Subjects")
