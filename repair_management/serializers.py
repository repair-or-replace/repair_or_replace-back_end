# repair_management/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Property, Appliance, Repairs, Investments, ApplianceApi, Order, Payment 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RepairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repairs
        fields = '__all__'

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'

class ApplianceSerializer(serializers.ModelSerializer):
    repairs = serializers.SerializerMethodField()
    investments = serializers.SerializerMethodField()
    total_repair_cost = serializers.SerializerMethodField()
    total_investment_cost = serializers.SerializerMethodField()
    repairs_exceed_cost = serializers.SerializerMethodField()

    class Meta:
        model = Appliance
        fields = '__all__'


    def get_repairs(self, obj):
        return RepairsSerializer(
            obj.repairs.filter(user=obj.user), many=True
        ).data

    def get_investments(self, obj):
        return InvestmentsSerializer(
            obj.investments.filter(user=obj.user), many=True
        ).data

    def get_total_repair_cost(self, obj):
        return sum(repair.cost for repair in obj.repairs.all())

    def get_total_investment_cost(self, obj):
        return sum(investment.cost for investment in obj.investments.all())

    def get_repairs_exceed_cost(self, obj):
        appliance_api_data = ApplianceApi.objects.filter(model=obj.model, brand=obj.brand).first()
        if not appliance_api_data:
            return None
        appliance_cost = appliance_api_data.lowest_listed_price or appliance_api_data.msrp
        if appliance_cost is None:
            return None
        return self.get_total_repair_cost(obj) > appliance_cost


class PropertySerializer(serializers.ModelSerializer):
    appliances = ApplianceSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'address_line_1', 'address_line_2', 'city', 'state', 'zipcode', 'home_type', 'year_built', 
            'default_image', 'user_uploaded_image', 'created_at', 'user', 'appliances'
        ]

class UserPropertySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'properties']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'properties']

class ApplianceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplianceApi
        fields = '__all__'

