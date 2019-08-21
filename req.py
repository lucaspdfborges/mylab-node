import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
params = {'probe_hash': '12567f7bb9305e01fdfc2300408c3dfdf390fadfee'}
r = requests.get(url, params=params, headers=headers)
r.text
