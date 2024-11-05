# from rest_framework import serializers
# from.models import Property, Appliance, Repairs, Investments, ApplianceApi
# from django.contrib.auth.models import User

# #this file tells us how to turn our model into JSON data
# class PropertySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Property
#         fields = [
#             'id',
#             'address_line_1',
#             'address_line_2',
#             'city',
#             'state',
#             'zipcode',
#             'home_type',
#             'year_built',
#             'user',
#             'default_image',
#             'user_uploaded_image',
#             'created_at',
#             'image',  # This is the method that returns the appropriate image URL
#         ]
#         read_only_fields = ['default_image', 'created_at', 'image']

#     def update(self, instance, validated_data):
#         # Handle image upload
#         if 'user_uploaded_image' in validated_data:
#             # Remove the old image if a new one is uploaded
#             if instance.user_uploaded_image:
#                 instance.user_uploaded_image.delete(save=False)
#             instance.user_uploaded_image = validated_data['user_uploaded_image']

#         # Update other fields
#         instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
#         instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
#         instance.city = validated_data.get('city', instance.city)
#         instance.state = validated_data.get('state', instance.state)
#         instance.zipcode = validated_data.get('zipcode', instance.zipcode)
#         instance.home_type = validated_data.get('home_type', instance.home_type)
#         instance.year_built = validated_data.get('year_built', instance.year_built)
#         instance.save()
#         return instance


# class UserPropertySerializer(serializers.ModelSerializer):
#     properties = PropertySerializer(many=True, read_only=True)  # 

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'properties']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

        
# # class ApplianceSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Appliance
# #         fields = '__all__'

# class ApplianceSerializer(serializers.ModelSerializer):
#     expected_end_of_life = serializers.SerializerMethodField()

#     class Meta:
#         model = Appliance
#         fields = ['id', 'name', 'purchase_date', 'typical_lifespan_years', 'expected_end_of_life']

#     def get_expected_end_of_life(self, obj):
#         return obj.expected_end_of_life()

# class RepairsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Repairs
#         fields = '__all__'

# class InvestmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Investments
#         fields = '__all__'

# class ApplianceApiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApplianceApi
#         fields = '__all__'



from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Property, Appliance, Repairs, Investments, ApplianceApi 



class ApplianceSerializer(serializers.ModelSerializer):
    repairs = serializers.SerializerMethodField()
    investments = serializers.SerializerMethodField()

    class Meta:
        model = Appliance
        fields = [
            'id', 'name', 'appliance_type', 'brand', 'model', 'property', 'user',
            'purchase_date', 'current_status', 'exp_end_of_life', 'repairs', 'investments'
        ]

    def get_repairs(self, obj):
        # Filter repairs by both the appliance and its associated user
        return RepairsSerializer(
            obj.repairs.filter(user=obj.user), many=True
        ).data

    def get_investments(self, obj):
        # Filter investments by both the appliance and its associated user
        return InvestmentsSerializer(
            obj.investments.filter(user=obj.user), many=True
        ).data


class PropertySerializer(serializers.ModelSerializer):
    appliances = ApplianceSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'address_line_1', 'address_line_2', 'city', 'state', 'zipcode', 'home_type', 'year_built', 
            'default_image', 'user_uploaded_image', 'created_at', 'user', 'appliances'
        ]


class RepairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repairs
        fields = '__all__'


class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'



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