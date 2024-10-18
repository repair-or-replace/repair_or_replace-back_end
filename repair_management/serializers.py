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

'''
from rest_framework import serializers
from .models import Property, Appliance, Repairs, Investments
from django.contrib.auth.models import User

# User Seri
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

# Property Seri
class PropertySerializer(serializers.ModelSerializer):  
    user = UserSerializer(read_only=True)   # Nested User 序列化器

    class Meta:
        model = Property
        fields = '__all__'

# Appliance Seri
class ApplianceSerializer(serializers.ModelSerializer):
    # property = PropertySerializer(read_only=True)  # Nested Property Serialiser
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Appliance
        fields = '__all__'

# Repairs Seri
class RepairsSerializer(serializers.ModelSerializer):
    # appliance = ApplianceSerializer(read_only=True)  # Nested Appliance Seri

    class Meta:
        model = Repairs
        fields = '__all__'

# Investments Seri
class InvestmentsSerializer(serializers.ModelSerializer):
    appliance = ApplianceSerializer(read_only=True)  # Nested Appliance Seri

    class Meta:
        model = Investments
        fields = '__all__'
'''

