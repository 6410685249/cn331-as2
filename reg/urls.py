from django.urls import path

from . import views

app_name = 'reg'
urlpatterns = [
    path('', views.Quota, name='Quota'),
    path('Add/Quota/<int:code>', views.Add_Quota, name="Add_quota"),
]