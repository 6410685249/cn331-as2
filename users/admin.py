from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAccount(admin.ModelAdmin):
    filter_horizontal = ['subjects']

admin.site.register(Student, StudentAccount)