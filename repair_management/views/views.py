from rest_framework import viewsets, status
from django.contrib.auth.models import User
from repair_management.models import Property, Appliance, Repairs, Investments, AppApiInfo
from repair_management.serializers import PropertySerializer, ApplianceSerializer, RepairsSerializer, InvestmentsSerializer, AppApiInfoSerializer, UserSerializer, UserPropertySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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


@method_decorator(csrf_exempt, name='dispatch')
class DecodeApplianceView(APIView):
    def post(self, request):
        data = request.data
        print(f"Received decoded_data: {data}")


        #extract details from request dta
        model = data.get('model')
        property_id = data.get('property_id')
        user_id = data.get('user')
        purchase_date = data.get('purchase_date')
        print(f"Property ID: {property_id}")
        print("user:", user_id)


        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user_instance = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)

        #check if appliace with this model/sku # exists in user's Appliance table
        existing_appliance = Appliance.objects.filter(model=model, property=property_instance).first()
        if existing_appliance:
            return JsonResponse({'message': 'Appliance already exists in this property'})

        #chcekc if info already exists in Appliance API table
        existing_info = ApplianceApi.objects.filter(model=model).first()
        if existing_info:
            return JsonResponse({'message': 'Appliance already exists in the Appliance API table'})
              
        
        #if exact appliance is not found in Appliance API  table, do the following

        headers = {
            "accept": "application/json",
            "Authorization" : "Bearer QWtZTDlsbTUrTGhPanBLZVRKblVYaEZoN3M5V3BKYWVNOFRJVStVVk1ZUWhMM3RwOEZRUVZNZDBqNmpncFFsaXJ4TEIwZWVQMUlVQXN5RkdDNFFYOFlTTFR5TDA2NGUxWnRoeG8vbmh0QWtDOW13NUsvRTJObDdPY21oeXVnMVR3a3ZRNE1hS1NhK2ZqNGVLaitIVng3ekd3NW5HQ3g5N0hONjlpdytmM0ZEV2FUZG10c3c3QURnRStCZm9rYzB1anpLUjdpUW90SUpTcXdtWmRVTU5UZz09"
        }
        json_data = {
            'model': model
        }

        
        url = f"https://api.appliance-data.com/product?sku={model}"
        response = requests.get(url, headers=headers)

        # print(f"Received response from API: Status {response.status_code}")
        # print(f"Response content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            decoded_data = data.get('data')           

            #save new decoded_data to ApplianceApi table
            ApplianceApi.objects.create(
                brand=decoded_data[0]['brand']['brand_name'],
                model=decoded_data[0].get('sku'),  
                description=decoded_data[0].get('name'),  
                category_name=decoded_data[0].get('category', {}).get('category_name'),  
                detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),  # Ame
                color=decoded_data[0].get('color'),  # Accessing color
                product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,  # first product image URL
                product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,  # e first product document URL
                product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,  # second product document URL
                lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],  
                home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],  
                msrp=decoded_data[0].get('price', {}).get('msrp', 0),
            )


            Appliance.objects.create(
                appliance_type=decoded_data[0].get('category', {}).get('category_name'),
                brand=decoded_data[0]['brand']['brand_name'],
                model=decoded_data[0].get('sku'),
                property=property_instance,
                user=user_instance,
                exp_end_of_life= '9999-12-31',
                purchase_date= purchase_date,
                current_status='working',  # default status is working
                cost=decoded_data[0].get('price',{}).get('msrp',0),
        )

            return JsonResponse({'status': 'added', 'decoded_data': decoded_data})

        return JsonResponse(response.json(), status=response.status_code)
    
    def get(self, request):
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
