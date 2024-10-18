1. Repair or Replace ERD(click the img.png)

![img.png](img.png)

2. Follow the ERD, create the models.py
use Django DRF

from django.db import models
from django.contrib.auth.models import User 


class Property(models.Model):
    HOME_TYPE_CHOICES = [
        ('single', 'Single Family'),
        ('multi', 'Multi Family'),
        ('condo', 'Condo'),
        ('apartment', 'Apartment'),
        ('other', 'Other')
    ]

    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    home_type = models.CharField(max_length=25, choices=HOME_TYPE_CHOICES)
    year_built = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')  # link to User
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}"

class Appliance(models.Model):
    STATUS_CHOICES = [
        ('working', 'Working'),
        ('needs repair', 'Needs Repair'),
        ('broken', 'Broken'),
        ('replaced', 'Replaced')
    ]
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='appliances')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appliances') 
    exp_end_of_life = models.DateField()
    purchase_date = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES) #
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.model})"
    
class Repairs(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='repairs')
    repair_date = models.DateField()
    repaired_by = models.CharField(max_length=250)
    repaired_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appliance} ({self.repair_date})"

class Investments(models.Model):
    INVESTMENT_CHOICES = [
        ('replacement', 'Replacement'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('upgrade', 'Upgrade')
    ]
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='investments')  # Use ForeignKey
    investment_type = models.CharField(max_length=25, choices=INVESTMENT_CHOICES)
    investment_date = models.DateField()
    investment_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appliance} ({self.investment_type})"


class ApplianceDetailsFromAPI(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"ApplianceDetailsFromAPI {self.id} at {self.created_at}"



3. According to the models, create the serializers.py

from rest_framework import serializers
from.models import Property, Appliance, Repairs, Investments, ApplianceDetailsFromAPI, CustomUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance
        fields = '__all__'

class RepairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repairs
        fields = '__all__'

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'

class ApplianceDetailsFromAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplianceDetailsFromAPI
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


4. Create the views.py

from rest_framework import viewsets
from django.contrib.auth.models import User
from.models import Property, Appliance, Repairs, Investments, ApplianceDetailsFromAPI, CustomUser
from.serializers import PropertySerializer, ApplianceSerializer, RepairsSerializer, InvestmentsSerializer, ApplianceDetailsFromAPISerializer, CustomUserSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly

class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes = []

class RepairsViewSet(viewsets.ModelViewSet):
    queryset = Repairs.objects.all()
    serializer_class = RepairsSerializer
    permission_classes = []

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    permission_classes = []

class ApplianceDetailsFromAPIViewSet(viewsets.ModelViewSet):
    queryset = ApplianceDetailsFromAPI.objects.all()
    serializer_class = ApplianceDetailsFromAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

5. Ceate urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from.views import PropertyViewSet, ApplianceViewSet, RepairsViewSet, InvestmentsViewSet, ApplianceDetailsFromAPIViewSet, CustomUserViewSet, UserViewSet

router = DefaultRouter()
router.register('properties', PropertyViewSet)
router.register('appliances', ApplianceViewSet)
router.register('repairs', RepairsViewSet)
router.register('investments', InvestmentsViewSet)
router.register('appliance-details-from-api', ApplianceDetailsFromAPIViewSet)
# router.register('users', CustomUserViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

6. Test on Postman

Start the server
python manage.py runserver
open Postman, 
Test the user first
The following is an example of the steps to perform CRUD operations on users in Postman:
1). Create a user (POST request)
Open Postman.
POST  http://127.0.0.1:8000/api/users/
Enter the following JSON data to represent a new user:
json
{
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
}

2). Query user (GET request)
http://127.0.0.1:8000/api/users/
to get a list of all users, 
http://127.0.0.1:8000/api/users/{user_id}
get information about a single user.

3). Update User (PUT/PATCH Request)
http://127.0.0.1:8000/api/users/{user_id}/.
Enter the following JSON data to represent the user information to be updated:
json
{
    "username": "updateduser",
    "email": "updateduser@example.com"
}
Click Sendthe button to send the request. If the update is successful, you will receive a response with a status code of 200 (OK) and the response body contains the updated user information.
4). Deleting a user (DELETE request)
Create a new request and set the request method to DELETE.
Enter the API endpoint address of the user you want to delete, such as http://127.0.0.1:8000/api/users/{user_id}/.
Click Sendthe button to send the request. If the deletion is successful, you will receive a response with status code 204 (No Content).