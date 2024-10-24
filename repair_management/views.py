from rest_framework import viewsets
from django.contrib.auth.models import User
from.models import Property, Appliance, Repairs, Investments, AppApiInfo, CustomUser
from.serializers import PropertySerializer, ApplianceSerializer, RepairsSerializer, InvestmentsSerializer, AppApiInfoSerializer, CustomUserSerializer, UserSerializer
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

class AppApiInfoViewSet(viewsets.ModelViewSet):
    queryset = AppApiInfo.objects.all()
    serializer_class = AppApiInfoSerializer
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
        print(f"Received data: {data}")
        print(f"User: {request.user}")


        #extract details from request dta
        make = data.get('make')
        model = data.get('model')
        serial_number = data.get('serial_number')
        user = request.user #get user submitting form
        property_id = data.get('property_id')
        print(f"Property ID: {property_id}")


        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)


        #chcekc if info already exists in AppApiInfo table
        existing_info = AppApiInfo.objects.filter(make=make, serial=serial_number, model=model).first()

        if existing_info:
            return JsonResponse({'status': 'found', 'data': {
                'make': existing_info.make,
                'model': existing_info.model,
                'serial': existing_info.serial,
                'most_likely_year': existing_info.most_likely_year,
                'average_listed_price': str(existing_info.average_listed_price),
                'full_date':existing_info.full_date.isoformat()
            }})
        
        #if exact appliance is not found in AppApiInfo table

        headers = {
            'Authorization': 'Bearer o2RKpcz05F28TLva6ghPOQ6dCaBwJJEjebupGCV3h69RirpDOT7VFgUFwx8N',
            'Accept': 'application/json',
        }
        json_data = {
            'make': make,
            'serial': serial_number,
            'model': model
        }
        
        print(f"Sending request to API with data: {json_data}")
        response = requests.get('https://homespy.io/api/decode', headers=headers, json=json_data)

        print(f"Received response from API: Status {response.status_code}")
        print(f"Response content: {response.text}")

        if response.status_code == 200:
            api_data = response.json()
            decoded_data = api_data.get('result', {}).get('decoded',{})

            most_likely_year = str(decoded_data.get('mostLikelyYear')) 
            year_options = decoded_data.get('yearOptions')
            full_date_str = year_options[most_likely_year].get('fullDate')

            print(year_options)
            print()

            print(f"Creating AppApiInfo with data: {decoded_data}")

            #save new data to AppApiInfo table
            AppApiInfo.objects.create(
                make=decoded_data.get('make'),
                model=decoded_data.get('model'),
                serial=decoded_data.get('serial'),
                description=decoded_data.get('details', {}).get('description'),
                most_likely_year=most_likely_year,
                average_listed_price=decoded_data.get('details', {}).get('averageListedPrice', 0.0),
                full_date=full_date_str,
                color=decoded_data.get('details', {}).get('color'),
                type=decoded_data.get('details', {}).get('type')
            )

            appliance = Appliance.objects.create(
            appliance_type=decoded_data.get('details',{}).get('type'),
            model=decoded_data.get('model'),
            make=decoded_data.get('make'),
            serial_number=decoded_data.get('serial'),
            property=property_instance,
            user=user,
            exp_end_of_life=full_date_str,  #
            purchase_date=data.get('purchase_date'),  # Extract from the request data
            current_status=data.get('current_status', 'working'),  # default status of working
            cost=data.get('cost', 0.0),
        )

            return JsonResponse({'status': 'added', 'data': decoded_data})

        return JsonResponse(response.json(), status=response.status_code)
    
    def get(self, request):
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
