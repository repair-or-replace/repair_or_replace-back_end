from rest_framework import viewsets
from django.contrib.auth.models import User  # Import the default User model
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from repair_management.models import Property, Appliance, Repairs, Investments, AppApiInfo
from repair_management.serializers import (
    PropertySerializer, ApplianceSerializer, RepairsSerializer,
    InvestmentsSerializer, AppApiInfoSerializer, UserSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RepairsViewSet(viewsets.ModelViewSet):
    queryset = Repairs.objects.all()
    serializer_class = RepairsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AppApiInfoViewSet(viewsets.ModelViewSet):
    queryset = AppApiInfo.objects.all()
    serializer_class = AppApiInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
