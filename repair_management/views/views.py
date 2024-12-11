from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
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
from rest_framework.decorators import action

from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 401:  # Unauthenticated
        # response.data['login_url'] = "https://repair-or-replace-back-end.onrender.com/api/login"
        response.data['login_url'] = "https://127.0.0.1:8000/api/login"

    return response


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

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


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()

        # Delete all associated with the user
        user.properties.all().delete()
        user.appliances.all().delete()
        user.repairs.all().delete()
        user.investments.all().delete()

        # Finally, delete the user account
        user.delete()
        return Response({"detail": "User and associated data deleted successfully."}, status=204)



class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

# class RepairsViewSet(viewsets.ModelViewSet):
#     queryset = Repairs.objects.all()
#     serializer_class = RepairsSerializer

class RepairsViewSet(viewsets.ModelViewSet):
    queryset = Repairs.objects.all()
    serializer_class = RepairsSerializer

    def get_queryset(self):
        # 获取查询参数 appliance
        appliance_id = self.request.query_params.get('appliance')
        if appliance_id:
            return Repairs.objects.filter(appliance_id=appliance_id)  # 
        return super().get_queryset()  # 


class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer


class ApplianceApiViewSet(viewsets.ModelViewSet):
    queryset = ApplianceApi.objects.all()
    serializer_class = ApplianceApiSerializer

