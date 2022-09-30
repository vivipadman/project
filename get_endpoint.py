import requests
import json

url = ""

payload={}
headers = {
  'accountid': '',
  'Accept': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

resp = json.loads(response.text)
# print(type(resp))

print("Is the device deleted from Nebula console: "+ str(resp['is_deleted']))
# print(resp['is_deleted'])

# for element in resp:
#   print(element)