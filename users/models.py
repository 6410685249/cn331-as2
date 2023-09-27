from django.db import models
# from ..admin.models import Subject
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=6)
    professor = models.CharField(max_length=128)
    quota = models.IntegerField(default=0)
    seat = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)
    # subjects = models.ManyToManyField(Subject, blank=True, related_name="list Subjects")
