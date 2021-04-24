import requests
import json

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def PrintBytesAsJSON(bytes):
    print(json.dumps(json.loads(bytes), indent=2))

response = requests.patch(
    url = 'https://192.168.1.90/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1',
    auth = ('admin', 'admin'),
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    },
    data = json.dumps({
    'Cisco-IOS-XE-native:GigabitEthernet': {
     'ip': {
        'address': {
         'primary': {
          'address': '192.168.1.230',
           'mask': '255.255.255.0'
          }
         }
        }
       }
   }),

    verify = False)

print('Response Code: ' + str(response.status_code))
