from rest_framework import serializers

from.models import Property, Appliance, Repairs, Investments, ApplianceApi
from django.contrib.auth.models import User

#this file tells us how to turn our model into JSON data

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class UserPropertySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)  # 

    class Meta:
        model = User
        fields = ['username', 'email', 'properties']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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

class ApplianceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplianceApi
        fields = '__all__'

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'


