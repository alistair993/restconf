import requests
import json

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def PrintBytesAsJSON(bytes):
    print(json.dumps(json.loads(bytes), indent=2))

response = requests.put(
    url = 'https://1.1.1.1/restconf/data/native/ntp/server/',
    auth = ('admin', 'pass'),
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    },
    data = json.dumps({
  'Cisco-IOS-XE-ntp:server': {
    'server-list': [
      {
        'ip-address': '7.7.7.7'
      },
      {
        'ip-address': '1.1.1.1'
      }
    ]
  }
}
),

    verify = False)

print('Response Code: ' + str(response.status_code))

