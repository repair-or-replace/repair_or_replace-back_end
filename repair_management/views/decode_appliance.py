# from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from django.shortcuts import render
# import requests
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from repair_management.models import Property, Appliance, ApplianceApi
# from django.conf import settings


# def add_appliance_view(request):
#     print("add_appliance_view called")  # Debug print
#     return render(request, 'add_appliance.html')


# @method_decorator(csrf_exempt, name='dispatch')
# class DecodeApplianceView(APIView):
#     def post(self, request):
#         data = request.data
#         print(f"Received decoded_data: {data}")


#         #extract details from request dta
#         model = data.get('model')
#         property_id = data.get('property_id')
#         user_id = data.get('user')
#         purchase_date = data.get('purchase_date')
#         print(f"Property ID: {property_id}")
#         print("user:", user_id)


#         try:
#             property_instance = Property.objects.get(id=property_id)
#         except Property.DoesNotExist:
#             return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             user_instance = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)

#         #check if appliace with this model/sku # exists in user's Appliance table
#         existing_appliance = Appliance.objects.filter(model=model, property=property_instance).first()
#         if existing_appliance:
#             return JsonResponse({'message': 'Appliance already exists in this property'})

#         #chcekc if info already exists in Appliance API table
#         existing_info = ApplianceApi.objects.filter(model=model).first()
#         if existing_info:
#             return JsonResponse({'message': 'Appliance already exists in the Appliance API table'})
              
        
#         #if exact appliance is not found in Appliance API  table, do the following

#         headers = {
#             "accept": "application/json",
#             "Authorization" : settings.AUTH_KEY
#         }
#         json_data = {
#             'model': model
#         }

        
#         url = f"https://api.appliance-data.com/product?sku={model}"
#         response = requests.get(url, headers=headers)

#         # print(f"Received response from API: Status {response.status_code}")
#         # print(f"Response content: {response.text}")

#         if response.status_code == 200:
#             data = response.json()
#             decoded_data = data.get('data')           

#             #save new decoded_data to ApplianceApi table
#             ApplianceApi.objects.create(
#                 brand=decoded_data[0]['brand']['brand_name'],
#                 model=decoded_data[0].get('sku'),  
#                 description=decoded_data[0].get('name'),  
#                 category_name=decoded_data[0].get('category', {}).get('category_name'),  
#                 detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),  # Ame
#                 color=decoded_data[0].get('color'),  # Accessing color
#                 product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,  # first product image URL
#                 product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,  # e first product document URL
#                 product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,  # second product document URL
#                 lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],  
#                 home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],  
#                 msrp=decoded_data[0].get('price', {}).get('msrp', 0),
#             )


#             Appliance.objects.create(
#                 appliance_type=decoded_data[0].get('category', {}).get('category_name'),
#                 brand=decoded_data[0]['brand']['brand_name'],
#                 model=decoded_data[0].get('sku'),
#                 property=property_instance,
#                 user=user_instance,
#                 exp_end_of_life= '9999-12-31',
#                 purchase_date= purchase_date,
#                 current_status='working',  # default status is working
#                 cost=decoded_data[0].get('price',{}).get('msrp',0),
#         )

#             return JsonResponse({'status': 'added', 'decoded_data': decoded_data})

#         return JsonResponse(response.json(), status=response.status_code)
    
#     def get(self, request):
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




# # from rest_framework.permissions import AllowAny
# # from django.contrib.auth.models import User
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from django.http import JsonResponse
# # from django.shortcuts import render
# # import requests
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # from repair_management.models import Property, Appliance, ApplianceApi
# # from django.conf import settings


# # def add_appliance_view(request):
# #     print("add_appliance_view called")  # Debug print
# #     return render(request, 'add_appliance.html')

# # @method_decorator(csrf_exempt, name='dispatch')
# # class DecodeApplianceView(APIView):
# #     permission_classes = [AllowAny]

# #     def post(self, request):
# #         print("CSRF Exempt Applied")
# #         print("DecodeApplianceView POST method called")
        
# #         print("Received Data:", request.data)
# #         data = request.data
# #         print(f"Received decoded_data: {data}")
        


# #         #extract details from request dta
# #         model = data.get('model')
# #         property_id = data.get('property_id')
# #         user_id = data.get('user')
# #         purchase_date = data.get('purchase_date')
# #         print(f"Property ID: {property_id}")
# #         print("user:", user_id)


# #         try:
# #             property_instance = Property.objects.get(id=property_id)
# #         except Property.DoesNotExist:
# #             return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)
        
# #         try:
# #             user_instance = User.objects.get(id=user_id)
# #         except User.DoesNotExist:
# #             return JsonResponse({'error': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)

# #         #check if appliace with this model/sku # exists in user's Appliance table
# #         existing_appliance = Appliance.objects.filter(model=model, property=property_instance).first()
# #         if existing_appliance:
# #             return JsonResponse({'message': 'Appliance already exists in this property'})

# #         #chcekc if info already exists in Appliance API table
# #         existing_info = ApplianceApi.objects.filter(model=model).first()
# #         if existing_info:
# #             return JsonResponse({'message': 'Appliance already exists in the Appliance API table'})
              
        
# #         #if exact appliance is not found in Appliance API  table, do the following

# #         headers = {
# #             "accept": "application/json",
# #             "Authorization" : settings.AUTH_KEY
# #         }
# #         json_data = {
# #             'model': model
# #         }

        
# #         url = f"https://api.appliance-data.com/product?sku={model}"
# #         response = requests.get(url, headers=headers)

# #         # print(f"Received response from API: Status {response.status_code}")
# #         # print(f"Response content: {response.text}")

# #         if response.status_code == 200:
# #             data = response.json()
# #             decoded_data = data.get('data')           

# #             #save new decoded_data to ApplianceApi table
# #             ApplianceApi.objects.create(
# #                 brand=decoded_data[0]['brand']['brand_name'],
# #                 model=decoded_data[0].get('sku'),  
# #                 description=decoded_data[0].get('name'),  
# #                 category_name=decoded_data[0].get('category', {}).get('category_name'),  
# #                 detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),  # Ame
# #                 color=decoded_data[0].get('color'),  # Accessing color
# #                 product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,  # first product image URL
# #                 product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,  # e first product document URL
# #                 product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,  # second product document URL
# #                 lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],  
# #                 home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],  
# #                 msrp=decoded_data[0].get('price', {}).get('msrp', 0),
# #             )


# #             Appliance.objects.create(
# #                 name=decoded_data[0].get('name'),  
# #                 appliance_type=decoded_data[0].get('category', {}).get('category_name'),
# #                 brand=decoded_data[0]['brand']['brand_name'],
# #                 model=decoded_data[0].get('sku'),
# #                 property=property_instance,
# #                 user=user_instance,
# #                 exp_end_of_life= '9999-12-31',
# #                 purchase_date= purchase_date,
# #                 product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None, 
# #                 current_status='working',  # default status is working
# #                 cost=decoded_data[0].get('price',{}).get('msrp',0),
# #         )

# #             return JsonResponse({'status': 'added', 'decoded_data': decoded_data})

# #         return JsonResponse(response.json(), status=response.status_code)
    
# #     def get(self, request):
# #         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from repair_management.models import Property, Appliance, ApplianceApi
# from django.conf import settings
# import requests


# def add_appliance_view(request):
#     print("add_appliance_view called")  # Debug print
#     return render(request, 'add_appliance.html')


# @method_decorator(csrf_exempt, name='dispatch')
# class DecodeApplianceView(APIView):
#     def post(self, request):
#         data = request.data
#         print(f"Received decoded_data: {data}")

#         # Extract details from request data
#         model = data.get('model')
#         property_id = data.get('property_id')
#         user_id = data.get('user')
#         purchase_date = data.get('purchase_date')
#         print(f"Property ID: {property_id}")
#         print("user:", user_id)

#         try:
#             property_instance = Property.objects.get(id=property_id)
#         except Property.DoesNotExist:
#             return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user_instance = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if appliance with this model/sku already exists in user's Appliance table
#         existing_appliance = Appliance.objects.filter(model=model, property=property_instance).first()
#         # if existing_appliance:
#         #     return JsonResponse({'message': 'Appliance already exists in this property'})

#         # Check if info already exists in ApplianceApi table
#         existing_info = ApplianceApi.objects.filter(model=model).first()
#         # if existing_info:
#         #     return JsonResponse({
#         #         'message': 'Appliance already exists in the Appliance API table',
#         #         'existing_appliance': {
#         #             'brand': existing_info.brand,
#         #             'model': existing_info.model,
#         #             'description': existing_info.description,
#         #             'category': existing_info.category_name,
#         #         }
#         #     })

#         # Attempt to fetch data from external API
#         url = f"https://api.appliance-data.com/product?sku={model}"
#         headers = {
#             "accept": "application/json",
#             "Authorization": settings.AUTH_KEY
#         }

#         print(f"Calling External API: {url}")
#         response = requests.get(url, headers=headers)
#         print(f"External API Response: {response.status_code}, {response.text}")

#         if response.status_code == 200:
#             data = response.json()
#             decoded_data = data.get('data')
#         else:
#             print("External API failed. Falling back to simulated data.")
#             # Simulated data in case API call fails
#             decoded_data = [{
#                 "brand": {"brand_name": "TestBrand"},
#                 "sku": model,
#                 "name": "TestDescription",
#                 "category": {"category_name": "TestCategory"},
#                 "detail_category": {"detail_category_name": "TestDetailCategory"},
#                 "color": "White",
#                 "product_images": [],
#                 "product_documents": [],
#                 "price": {
#                     "lap": {
#                         "lowest_price": 100.0,
#                         "homedepot_price": 110.0
#                     },
#                     "msrp": 120.0
#                 }
#             }]

#         # Save new decoded_data to ApplianceApi table
#         ApplianceApi.objects.create(
#             brand=decoded_data[0]['brand']['brand_name'],
#             model=decoded_data[0].get('sku'),
#             description=decoded_data[0].get('name'),
#             category_name=decoded_data[0].get('category', {}).get('category_name'),
#             detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),
#             color=decoded_data[0].get('color'),
#             product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,
#             product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,
#             product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,
#             lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],
#             home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],
#             msrp=decoded_data[0].get('price', {}).get('msrp', 0),
#         )

#         # Save appliance data to Appliance table
#         appliance = Appliance.objects.create(
#             name=decoded_data[0].get('name'),
#             appliance_type=decoded_data[0].get('category', {}).get('category_name'),
#             brand=decoded_data[0]['brand']['brand_name'],
#             model=decoded_data[0].get('sku'),
#             property=property_instance,
#             user=user_instance,
#             exp_end_of_life="9999-12-31",
#             purchase_date=purchase_date,
#             product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,
#             current_status="working",  # Default status is working
#             cost=decoded_data[0].get('price', {}).get('msrp', 0),
#         )

#         return JsonResponse({
#             "status": "added",
#             "appliance": {
#                 "name": appliance.name,
#                 "model": appliance.model,
#                 "brand": appliance.brand,
#                 "category": appliance.appliance_type,
#                 "price": {
#                     "lowest_price": decoded_data[0]["price"]["lap"]["lowest_price"],
#                     "homedepot_price": decoded_data[0]["price"]["lap"]["homedepot_price"],
#                     "msrp": decoded_data[0]["price"]["msrp"]
#                 },
#                 "color": appliance.product_image or "Not available"
#             }
#         })

#     def get(self, request):
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)






from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from repair_management.models import Property, Appliance, ApplianceApi
from django.conf import settings
import requests


def add_appliance_view(request):
    print("add_appliance_view called")  # Debug print
    return render(request, 'add_appliance.html')

# @method_decorator(csrf_exempt, name='dispatch')
# class DecodeApplianceView(APIView):
#     def post(self, request):
#         data = request.data
#         print(f"Received decoded_data: {data}")

#         # Extract details from request data
#         model = data.get('model')
#         property_id = data.get('property_id')
#         user_id = data.get('user')
#         purchase_date = data.get('purchase_date')
#         print(f"Property ID: {property_id}")
#         print("user:", user_id)

#         try:
#             property_instance = Property.objects.get(id=property_id)
#         except Property.DoesNotExist:
#             return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user_instance = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if info already exists in ApplianceApi table
#         existing_info = ApplianceApi.objects.filter(model=model).first()

#         if existing_info:
#             print(f"Appliance model {model} found in ApplianceApi table. Using cached data.")
#         else:
#             # Attempt to fetch data from external API
#             url = f"https://api.appliance-data.com/product?sku={model}"
#             headers = {
#                 "accept": "application/json",
#                 "Authorization": settings.AUTH_KEY
#             }

#             print(f"Calling External API: {url}")
#             response = requests.get(url, headers=headers)
#             print(f"External API Response: {response.status_code}, {response.text}")

#             if response.status_code == 200:
#                 data = response.json()
#                 decoded_data = data.get('data')
#             else:
#                 print("External API failed. Falling back to simulated data.")
#                 # Simulated data in case API call fails
#                 decoded_data = [{
#                     "brand": {"brand_name": "TestBrand"},
#                     "sku": model,
#                     "name": "TestDescription",
#                     "category": {"category_name": "TestCategory"},
#                     "detail_category": {"detail_category_name": "TestDetailCategory"},
#                     "color": "White",
#                     "product_images": [],
#                     "product_documents": [],
#                     "price": {
#                         "lap": {
#                             "lowest_price": 100.0,
#                             "homedepot_price": 110.0
#                         },
#                         "msrp": 120.0
#                     }
#                 }]

#             # Save new decoded_data to ApplianceApi table
#             existing_info = ApplianceApi.objects.create(
#                 brand=decoded_data[0]['brand']['brand_name'],
#                 model=decoded_data[0].get('sku'),
#                 description=decoded_data[0].get('name'),
#                 category_name=decoded_data[0].get('category', {}).get('category_name'),
#                 detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),
#                 color=decoded_data[0].get('color'),
#                 product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,
#                 product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,
#                 product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,
#                 lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],
#                 home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],
#                 msrp=decoded_data[0].get('price', {}).get('msrp', 0),
#             )

#         # Save appliance data to Appliance table
#         appliance = Appliance.objects.create(
#             name=existing_info.description,
#             appliance_type=existing_info.category_name,
#             brand=existing_info.brand,
#             model=existing_info.model,
#             property=property_instance,
#             user=user_instance,
#             exp_end_of_life="9999-12-31",
#             purchase_date=purchase_date,

@method_decorator(csrf_exempt, name='dispatch')
class DecodeApplianceView(APIView):
    def post(self, request):
        data = request.data
        print(f"Received decoded_data: {data}")

        # Extract details from request data
        model = data.get('model')
        property_id = data.get('property_id')
        user_id = data.get('user')
        purchase_date = data.get('purchase_date')
        print(f"Property ID: {property_id}")
        print("user:", user_id)

        # Check if property exists
        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return JsonResponse({'error': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user exists
        try:
            user_instance = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the model already exists in ApplianceApi table
        existing_info = ApplianceApi.objects.filter(model=model).first()
        if existing_info:
            print(f"Appliance model {model} found in ApplianceApi table. Using cached data.")
        else:
            # Call external API
            url = f"https://api.appliance-data.com/product?sku={model}"
            headers = {
                "accept": "application/json",
                "Authorization": settings.AUTH_KEY
            }

            print(f"Calling External API: {url}")
            response = requests.get(url, headers=headers)
            print(f"External API Response: {response.status_code}, {response.text}")

            if response.status_code == 200:
                data = response.json()
                decoded_data = data.get('data')

                if not decoded_data:
                    return JsonResponse({
                        "error": "No data found for the given model from the external API."
                    }, status=status.HTTP_404_NOT_FOUND)

                # Save new data to ApplianceApi table
                existing_info = ApplianceApi.objects.create(
                    brand=decoded_data[0]['brand']['brand_name'],
                    model=decoded_data[0].get('sku'),
                    description=decoded_data[0].get('name'),
                    category_name=decoded_data[0].get('category', {}).get('category_name'),
                    detail_category_name=decoded_data[0].get('detail_category', {}).get('detail_category_name'),
                    color=decoded_data[0].get('color'),
                    product_image=decoded_data[0]['product_images'][0]['url'] if decoded_data[0]['product_images'] else None,
                    product_doc_1=decoded_data[0]['product_documents'][0]['url'] if decoded_data[0]['product_documents'] else None,
                    product_doc_2=decoded_data[0]['product_documents'][1]['url'] if len(decoded_data[0]['product_documents']) > 1 else None,
                    lowest_listed_price=decoded_data[0]["price"]["lap"]["lowest_price"],
                    home_depot_price=decoded_data[0]["price"]["lap"]["homedepot_price"],
                    msrp=decoded_data[0].get('price', {}).get('msrp', 0),
                )
            else:
                # If the external API fails
                return JsonResponse({
                    "error": "Failed to fetch data from the external API. Please try again later."
                }, status=status.HTTP_502_BAD_GATEWAY)

        # Save appliance data to Appliance table
        appliance = Appliance.objects.create(
            name=existing_info.description,
            appliance_type=existing_info.category_name,
            brand=existing_info.brand,
            model=existing_info.model,
            property=property_instance,
            user=user_instance,
            exp_end_of_life="2034-12-31",
            purchase_date=purchase_date,
           

            product_image=existing_info.product_image,
            current_status="working",  # Default status is working
            cost=existing_info.msrp,
        )

        return JsonResponse({
            "status": "added",
            "appliance": {
                "name": appliance.name,
                "model": appliance.model,
                "brand": appliance.brand,
                "category": appliance.appliance_type,
                "price": {
                    "lowest_price": existing_info.lowest_listed_price,
                    "homedepot_price": existing_info.home_depot_price,
                    "msrp": existing_info.msrp
                },
                "color": existing_info.color or "Not available"
            }
        })

    def get(self, request):
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
