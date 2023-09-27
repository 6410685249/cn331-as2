from django.db import models

# Create your models here.

class Subject(models.Model):
    SEMESTER = [
        ('first','1'),
        ('second','2'),
        ('third','3'),
        ('forth','4'),
        ('fifth','5'),
        ('summer','summer'),
    ]
    name = models.CharField(max_length=64)
    code = models.CharField(primary_key=True, max_length=6)
    professor = models.CharField(max_length=128)
    semester = models.CharField(max_length=6, choices=SEMESTER, default='1')
    year = models.CharField(max_length=4, default="2566")
    quota = models.BooleanField(default=False)
    seat = models.IntegerField()