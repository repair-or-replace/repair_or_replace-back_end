import requests

headers = {
      'Authorization': 'Bearer o2RKpcz05F28TLva6ghPOQ6dCaBwJJEjebupGCV3h69RirpDOT7VFgUFwx8N',
      'Accept': 'application/json',
      # Already added when you pass json=
      # 'Content-Type': 'application/json',
  }

json_data = {
      'make': 'GE', #will have to remove hardcoded variables and input user input
      'serial': 'VV135374G',
      'model': 'PTW600BSR1S',
  }

response = requests.get('https://homespy.io/api/decode', headers=headers, json=json_data)

print(response.text)
