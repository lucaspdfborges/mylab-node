import requests
import time
import math

url = 'http://127.0.0.1:8000/api/datum/'
headers = {'Authorization': 'Token fd191bd59fea5fcb466fc4b0f8a3e04d90e9a42c'}
data = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'value': '1', 'note':''}

data2 = {'probe_hash': 'c41efb16baf6ca11d5ccfec44483d642', 'min_value':'3','max_value':'', 'min_timestamp':'', 'max_timestamp':''}


def funcData(value):
    return {'probe_hash': '1a2a1b6e52da93dbcfe4b49cc6a585a0', 'value': str(value), 'note':''}

# for i in range(10):
#     data = funcData(math.pi*i/10)
#     r = requests.post(url, data=data, headers=headers)
#     time.sleep(1)



r = requests.get(url, params=data2, headers=headers)
print(r.text)
