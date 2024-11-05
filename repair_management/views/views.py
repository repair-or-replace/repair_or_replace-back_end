from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from repair_management.models import Property, Appliance, Repairs, Investments, ApplianceApi
from repair_management.serializers import (
    UserDetailSerializer,
    UserPropertySerializer,
    UserSerializer,
    PropertySerializer,
    ApplianceSerializer,
    RepairsSerializer,
    InvestmentsSerializer,
    ApplianceApiSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = []#

    def get_serializer_context(self):
        return {"request": self.request}
        
class UserPropertyViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPropertySerializer

    def list(self, request, pk=None):
        if pk:
            users = User.objects.filter(pk=pk)
        else:
            users = User.objects.all()
        serializer = UserPropertySerializer(users, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny] 


class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes = [AllowAny]


class RepairsViewSet(viewsets.ModelViewSet):
    queryset = Repairs.objects.all()
    serializer_class = RepairsSerializer
    permission_classes = [AllowAny]


class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    permission_classes = [AllowAny]


class ApplianceApiViewSet(viewsets.ModelViewSet):
    queryset = ApplianceApi.objects.all()
    serializer_class = ApplianceApiSerializer
    permission_classes = []  # AllowAny

