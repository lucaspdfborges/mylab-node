import requests
import time
import math
from random import randint

url = 'http://127.0.0.1:8000/api/hello/'
headers = {'Authorization': 'Token 5fb496972e75e3ce8ea14175b37d0742e3884b73'}

r = requests.get(url, headers=headers)
print(r.text)
