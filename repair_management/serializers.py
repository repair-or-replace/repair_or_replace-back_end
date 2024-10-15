from rest_framework import serializers
from .models import Property, Appliance, Repairs, Investments
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'email']

class PropertySerialier(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'
