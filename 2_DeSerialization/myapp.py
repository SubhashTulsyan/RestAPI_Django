import requests, json

a = {
    'name': 'Nidhi',
    'roll': 3211,
}
URL = 'http://127.0.0.1:8000'

aa = json.dumps(a)
print(aa)

r= requests.post(url=URL, data=aa)
print('r: ', r)
print('r json: ', r.json())
