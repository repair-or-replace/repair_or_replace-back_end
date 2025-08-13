# repair_management/views/order_views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from repair_management.models import (
    Property, Appliance, Repairs, Investments, ApplianceApi, Order, Payment
)
from repair_management.serializers import (
    UserDetailSerializer, UserPropertySerializer, UserSerializer,
    PropertySerializer, ApplianceSerializer, RepairsSerializer,
    InvestmentsSerializer, ApplianceApiSerializer,
    OrderSerializer, PaymentSerializer
)

from rest_framework.views import exception_handler

# Custom exception handler to include login redirect URL if 401
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None and response.status_code == 401:
        response.data['login_url'] = "https://127.0.0.1:8000/api/login"
    return response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class UserPropertyViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPropertySerializer

    def list(self, request, pk=None):
        users = User.objects.filter(pk=pk) if pk else User.objects.all()
        serializer = UserPropertySerializer(users, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.properties.all().delete()
        user.appliances.all().delete()
        user.repairs.all().delete()
        user.investments.all().delete()
        user.delete()
        return Response({"detail": "User and associated data deleted successfully."}, status=204)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer


class RepairsViewSet(viewsets.ModelViewSet):
    queryset = Repairs.objects.all()
    serializer_class = RepairsSerializer

    def get_queryset(self):
        appliance_id = self.request.query_params.get('appliance')
        if appliance_id:
            return Repairs.objects.filter(appliance_id=appliance_id)
        return super().get_queryset()


class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer

    def get_queryset(self):
        appliance_id = self.request.query_params.get('appliance')
        if appliance_id:
            return Investments.objects.filter(appliance_id=appliance_id)
        return super().get_queryset()


class ApplianceApiViewSet(viewsets.ModelViewSet):
    queryset = ApplianceApi.objects.all()
    serializer_class = ApplianceApiSerializer
