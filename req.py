import requests
import time
import math

url = 'http://127.0.0.1:8000/api/datum/'
headers = {'Authorization': 'Token 76c563009be5d758e98bf7e89572dad6ea578a28'}
data = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'value': '1', 'note':''}

def funcData(value):
    return {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'value': str(value), 'note':''}

for i in range(10):
    data = funcData(math.pi*i/10)
    r = requests.post(url, data=data, headers=headers)
    time.sleep(1)
