from django.urls import path

from . import views

app_name = 'reg'
urlpatterns = [
    path('', views.Quota, name='Quota'),
    path('Add/Quota/<str:code>', views.Add_Quota, name="Add_Quota"),
]