from django.contrib import admin
from .models import Subject
# Register your models here.
class SubjectManage(admin.ModelAdmin):
    filter_horizontal = ['students']

admin.site.register(Subject, SubjectManage)