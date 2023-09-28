from django.db import models
from administrator.models import Subject
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    FACULTY = [
        ('ทันตแพทย์','Dentistry'),
        ('พยาบาลศาสตร์','Nursing'),
        ('แพทยศาสตร์','Medicine'),
        ('เภสัชศาสตร์','Pharmaceutical Sciences'),
        ('ศึกษาศาสตร์','Education'),
        ('วิทยาศาสตร์','Science'),
        ('วิศวกรรมศาสตร์','Engineering'),
        ('สถาปัตยศาสตร์','Architecture'),
        ('นิเทศศาสตร์','Communication Arts'),
        ('นิติศาสตร์','Law'),
    ]
    # name = models.CharField(max_length=64)
    # surname = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(primary_key=True, max_length=10)
    status = models.BooleanField(default=False)
    faculty = models.CharField(max_length=128, choices=FACULTY, default="null")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="list_Subjects")
