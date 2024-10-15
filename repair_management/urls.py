from django.urls import path
from . import views

urlpatterns = [
    path('repairs/', views.RepairList.as_view(), name='repair-list'),
    path('properties/',views.PropertyList.as_view(), name= 'property-list')
]
