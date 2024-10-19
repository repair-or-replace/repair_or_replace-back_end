import requests

# url = "https://api.appliance-data.com/product"


# url = "https://api.appliance-data.com/product?sku=AEL36DFBLK&brand=AGA" #worked


url = "https://api.appliance-data.com/product?sku=PTD60EBSR0WS"




headers = {
    "accept": "application/json",
    "Authorization": "Bearer QWtZTDlsbTUrTGhPanBLZVRKblVYaEZoN3M5V3BKYWVNOFRJVStVVk1ZUWhMM3RwOEZRUVZNZDBqNmpncFFsaXJ4TEIwZWVQMUlVQXN5RkdDNFFYOFlTTFR5TDA2NGUxWnRoeG8vbmh0QWtDOW13NUsvRTJObDdPY21oeXVnMVR3a3ZRNE1hS1NhK2ZqNGVLaitIVng3ekd3NW5HQ3g5N0hONjlpdytmM0ZEV2FUZG10c3c3QURnRStCZm9rYzB1K21pUEtEV1hvZ3UvTkJuWnlRamhjUT09"
}

response = requests.get(url, headers=headers)

print(response.text)
