import requests
from requests.auth import HTTPBasicAuth

url = "https://api.appliance-data.com/product"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "public-key": "QWtZTDlsbTUrTGhPanBLZVRKblVYaEZoN3M5V3BKYWVNOFRJVStVVk1ZUWhMM3RwOEZRUVZNZDBqNmpncFFsaXJ4TEIwZWVQMUlVQXN5RkdDNFFYOFlTTFR5TDA2NGUxWnRoeG8vbmh0QWtDOW13NUsvRTJObDdPY21oeXVnMVR3a3ZRNE1hS1NhK2ZqNGVLaitIVng3ekd3NW5HQ3g5N0hONjlpdytmM0ZEV2FUZG10c3c3QURnRStCZm9rYzB1K21pUEtEV1hvZ3UvTkJuWnlRamhjUT09",
    "secret-key": "QWtZTDlsbTUrTGhPanBLZVRKblVYaEZoN3M5V3BKYWVNOFRJVStVVk1ZUWhMM3RwOEZRUVZNZDBqNmpncFFsaXJ4TEIwZWVQMUlVQXN5RkdDNFFYOFlTTFR5TDA2NGUxWnRoeG8vbmh0QWtDOW13NUsvRTJObDdPY21oeXVnMVR3a3ZRNE1hS1NhK2ZqNGVLaitIVng3ekd3NW5HQ3g5N0hONjlpdytmM0ZEV2FUZG10c3c3QURnRStCZm9rYzB1anpLUjdpUW90SUpTcXdtWmRVTU5UZz09"
}

auth = HTTPBasicAuth("christyhernandez", "C4FqEbiB%=b8")
response = requests.get(url, headers=headers, auth=auth)

print(response.status_code)
print(response.json())  # Use parentheses to properly call the method
print(response.text)
