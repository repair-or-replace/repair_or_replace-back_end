from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from repair_management.models import Property, Appliance, ApplianceApi
from django.conf import settings


def add_appliance_view(request):
    print("add_appliance_view called")
    return render(request, 'add_appliance.html')


@method_decorator(csrf_exempt, name='dispatch')
class DecodeApplianceView(APIView):
    def post(self, request):
        data = request.data
        print(f"Received decoded_data: {data}")

        # extract details from request dta
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

        # check if appliace with this model/sku # exists in user's Appliance table
        existing_appliance = Appliance.objects.filter(
            model=model, property=property_instance).first()
        if existing_appliance:
            return JsonResponse({'message': 'Appliance already exists in this property'})

        # chcekc if info already exists in Appliance API table
        existing_info = ApplianceApi.objects.filter(
            model__iexact=model).first()
        if not existing_info:
            headers = {
                "accept": "application/json",
                "Authorization": settings.AUTH_KEY
            }
            url = f"https://api.appliance-data.com/product?sku={model}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                decoded_data = data.get('data')

                # Save new decoded_data to ApplianceApi table
                existing_info = ApplianceApi.objects.create(
                    brand=decoded_data[0]['brand']['brand_name'],
                    model=decoded_data[0].get('sku'),
                    description=decoded_data[0].get('name'),
                    category_name=decoded_data[0].get(
                        'category', {}).get('category_name'),
                    detail_category_name=decoded_data[0].get(
                        'detail_category', {}).get('detail_category_name'),
                    color=decoded_data[0].get('color'),
                    product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,
                    product_doc_1=decoded_data[0]['product_documents'][0][
                        'url'] if decoded_data[0]['product_documents'] else None,
                    product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(
                        decoded_data[0]['product_documents']) > 1 else None,
                    lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],
                    home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],
                    msrp=decoded_data[0].get('price', {}).get('msrp', 0),
                )
            else:
                return JsonResponse(response.json(), status=response.status_code)
        # Create a new Appliance record
        new_appliance = Appliance.objects.create(
            name=existing_info.description,
            appliance_type=existing_info.category_name,
            brand=existing_info.brand,
            model=existing_info.model,
            property=property_instance,
            user=user_instance,
            exp_end_of_life='9999-12-31',
            purchase_date=purchase_date,
            product_image=existing_info.product_image,
            current_status='working',  # default status is working
            cost=existing_info.msrp,
        )

        return JsonResponse({'status': 'added', 'appliance': {
            'id': new_appliance.id,
            'name': new_appliance.name,
            'model': new_appliance.model,
            'current_status': new_appliance.current_status,
            'property': property_instance.id,
            'user': user_instance.id
        }})

    def get(self, request):
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
