import requests
import time
import math
from random import randint

url = 'http://127.0.0.1:8000/api/datum/'
headers = {'Authorization': 'Token 5fb496972e75e3ce8ea14175b37d0742e3884b73'}

data = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'value': '1', 'note':''}

data2 = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'min_value':'3','max_value':'', 'min_timestamp':'', 'max_timestamp':''}


def funcData(value):
    return {'probe_hash': 'ae2c9e08f48188dcba50a3a92b464936', 'value': str(value), 'note':''}

for i in range(15):
    data = funcData(math.pi*i/10+ int(randint(0,9))/2)
    r = requests.post(url, data=data, headers=headers)
    time.sleep(1)

# r = requests.get(url, params=data2, headers=headers)
# print(r.text)
