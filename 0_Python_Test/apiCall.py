import requests

URL = 'http://127.0.0.1:8000/api/students/'

res = requests.get(url=URL)

print(res.json())