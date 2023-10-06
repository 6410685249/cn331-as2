from django.urls import path

from . import views

app_name = 'reg'
urlpatterns = [
    path('', views.Quota, name='Quota'),
    path('Add/Quota/<str:code>', views.Add_Quota, name="Add_Quota"),
    path('Subject/page/', views.Subject_page, name="Subject_page")
]