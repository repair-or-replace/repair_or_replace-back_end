from rest_framework import viewsets
from django.contrib.auth.models import User
from.models import Property, Appliance, Repairs, Investments, AppApiInfo, CustomUser
from.serializers import PropertySerializer, ApplianceSerializer, RepairsSerializer, InvestmentsSerializer, AppApiInfoSerializer, CustomUserSerializer, UserSerializer
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

class AppApiInfoViewSet(viewsets.ModelViewSet):
    queryset = AppApiInfo.objects.all()
    serializer_class = AppApiInfoSerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly
