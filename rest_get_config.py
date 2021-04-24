import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://1.1.1.1/restconf/data/native'
headers = {'content-type': 'application/yang-data+json'}

inUsername = input("Username: ")
inUserPass = input("Password: ")

response = requests.get(url, headers=headers, auth=(inUsername, inUserPass), verify=False)

print(response)
print(response.text)
