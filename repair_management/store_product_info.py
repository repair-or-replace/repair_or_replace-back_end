import json
from .models import ProductInfo
from get_product import response

data = json.loads(response)
decoded = data['result']['decoded']
details = decoded['details']
year = decoded['mostLikelyYear']
year_options = decoded['yearOptions'][str(year)]

product = ProductInfo(
    make = decoded['make'],
    model = decoded['model'],
    serial = decoded['serial'],
    full_date = year ['fullDate'],
    description = decoded['description'],
    average_price = details['averageListedPrice']
)

product.save()
print("Data saved")