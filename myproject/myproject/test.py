import requests

__author__ = 'aGn'

token_url = "http://127.0.0.1:8000/api/login"
purchase_url = "http://127.0.0.1:8000/api/sampleapi"
auth_ = {"username": "your-username",
         "password": "your-password"}  # This is a Django user.

r1 = requests.post(token_url, data=auth_)
assert r1 and r1.ok and r1.status_code == 200 or 202
token_ = r1.json()['token']
header = {'Authorization': 'Token ' + token_}
r2 = requests.get(purchase_url, headers=header)
assert r2 and r2.ok and r2.status_code == 200 or 202
print(r2.text)
