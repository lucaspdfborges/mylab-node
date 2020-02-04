import requests
import time
import math
from random import randint

url = 'http://127.0.0.1:8000/api/datum/'
headers = {'Authorization': 'Token 5fb496972e75e3ce8ea14175b37d0742e3884b73'}

data2 = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'min_value':'3','max_value':'', 'min_timestamp':'', 'max_timestamp':''}


def funcData(value):
    return {'probe_hash': 'f01d51eadb0731c96fcb3d8855b12a5b', 'value': str(value), 'note':'ok'}

for i in range(2):
    data = funcData(1)
    r = requests.post(url, data=data, headers=headers)
    print(r.status_code)
    time.sleep(1)

# r = requests.get(url, params=data2, headers=headers)
# print(r.text)
