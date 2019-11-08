import requests
import time
import math
from random import randint

url = 'http://127.0.0.1:8000/api/datum/'
headers = {'Authorization': 'Token 5fb496972e75e3ce8ea14175b37d0742e3884b73'}

def funcData(value):
    return {'probe_hash': '38ca7d9fc6d488ac37f3b7dc3fb906ad', 'value': str(value), 'note':''}

def funcData2(value):
    return {'probe_hash': 'ae2c9e08f48188dcba50a3a92b464936', 'value': str(value), 'note':''}

for i in range(15):
    data = funcData(math.pi*i/10+ int(randint(0,9))/2)
    r = requests.post(url, data=data, headers=headers)
    time.sleep(1)

    data2 = funcData2(math.pi*i/10+ int(randint(0,9))/2)
    r2 = requests.post(url, data=data2, headers=headers)
    time.sleep(1)

# r = requests.get(url, params=data2, headers=headers)
# print(r.text)
