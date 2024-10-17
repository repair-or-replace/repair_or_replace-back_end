from django.urls import path
from . import views

#the paths of the endpoints
#this file maps URLs to view. 
#when a user accesses a specific URL, django check the urls.py to determine which view to call

urlpatterns = [
    path('repairs/', views.RepairList.as_view(), name='repair-list'),
    path('properties/',views.PropertyList.as_view(), name= 'property-list')
]
