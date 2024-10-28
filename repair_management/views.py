from rest_framework import viewsets
from django.contrib.auth.models import User
from.models import Property, Appliance, Repairs, Investments, ApplianceApi, CustomUser
from.serializers import PropertySerializer, ApplianceSerializer, RepairsSerializer, InvestmentsSerializer, ApplianceApiSerializer, CustomUserSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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

class ApplianceApiViewSet(viewsets.ModelViewSet):
    queryset = ApplianceApi.objects.all()
    serializer_class = ApplianceApiSerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [] #IsAuthenticatedOrReadOnly

class PropertyView(View):
    def get(self, request, property_id):
        property = Property.objects.get(id=property_id)
        return render (request, 'view_property.html', {'property':property})

def add_appliance_view(request):
    print("add_appliance_view called")  # Debug print
    return render(request, 'add_appliance.html')


@method_decorator(csrf_exempt, name='dispatch')
class DecodeApplianceView(APIView):
    def post(self, request):
        data = request.data
        print(f"Received decoded_data: {data}")
        print(f"User: {request.user}")


        #extract details from request dta
        model = data.get('model')
        user = request.user #get user submitting form
        property_id = data.get('property_id')
        print(f"Property ID: {property_id}")


        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)


        #chcekc if info already exists in Appliance table
        existing_info = ApplianceApi.objects.filter(model=model).first()

        if existing_info:
            return JsonResponse({'status': 'found', 'data': {
                'brand': existing_info.brand,
                'model': existing_info.model,
                'description': existing_info.description,
                'category': existing_info.category_name,
                'detail_category': existing_info.detail_category_name,
                'color': existing_info.color,
                'product_image': existing_info.product_image,
                'product_doc_1': existing_info.product_doc_1,
                'product_doc_2': existing_info.product_doc_2,
                'lowest_listed_price': existing_info.lowest_listed_price,
                'homedepot_price': existing_info.home_depot_price,
                'msrp': existing_info.msrp
            }})
        
        #if exact appliance is not found in AppApiInfo table

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
            # print("decoded_data", decoded_data)
            print("brand=",decoded_data[0]['brand']['brand_name'])
            print("category_name=",decoded_data[0].get('category', {}).get('category_name'))
            print("lowest_price =" , decoded_data[0]["price"]["lap"]["lowest_price"])
           

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
                user=user,
                exp_end_of_life= decoded_data[0].get('lifecycle', {}).get('exp_end_of_life'),
                purchase_date= '9999-12-31',
                current_status=decoded_data.get('current_status', 'working'),  # default status is working
                cost=decoded_data[0].get('price',{}).get('msrp',0),
        )

            return JsonResponse({'status': 'added', 'decoded_data': decoded_data})

        return JsonResponse(response.json(), status=response.status_code)
    
    def get(self, request):
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
