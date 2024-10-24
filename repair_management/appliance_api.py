import requests


headers = {
            "accept": "application/json",
            "Authorization" : "Bearer QWtZTDlsbTUrTGhPanBLZVRKblVYaEZoN3M5V3BKYWVNOFRJVStVVk1ZUWhMM3RwOEZRUVZNZDBqNmpncFFsaXJ4TEIwZWVQMUlVQXN5RkdDNFFYOFlTTFR5TDA2NGUxWnRoeG8vbmh0QWtDOW13NUsvRTJObDdPY21oeXVnMVR3a3ZRNE1hS1NhK2ZqNGVLaitIVng3ekd3NW5HQ3g5N0hONjlpdytmM0ZEV2FUZG10c3c3QURnRStCZm9rYzB1anpLUjdpUW90SUpTcXdtWmRVTU5UZz09"
        }


#filter by sku only

url = "https://api.appliance-data.com/product?sku=JVW5301SJSS"
response = requests.get(url, headers=headers)

#uncomment to see result data
#print(response.text)


#filter by brand only
# url = "https://api.appliance-data.com/product?brand=LG"
# response = requests.get(url, headers=headers)

#uncomment to see result data
# print(response.text)


url = "https://api.appliance-data.com/product?brand=LG&sku=LCG3611BD"
response = requests.get(url, headers=headers)

#uncomment to see result data
print(response.text)