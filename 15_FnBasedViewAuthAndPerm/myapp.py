import requests, json


URL = 'http://127.0.0.1:8000/getData1/'
headers = {'content-type': 'application/json'}
def getData(id = None):
    print('id: ', id)
    a = {}
    if id is not None:
        a = {
            'id': id,
        }
    js_data = json.dumps(a)
    print('js_data: ', js_data)

    r = requests.get(url=URL, data = js_data, headers=headers)
    print('r: ', r)
    print('r json: ', r.json())

def postData():
    data = {
        'name': 'apiviewK',
        'roll': '21',
    }

    res = requests.post(url=URL, data=json.dumps(data), headers=headers)
    print(res.json())
#postData()

def updateData():
    data = {
        'id': 10,
        'name': 'Raju',
    }
    data_json = json.dumps(data)
    res = requests.put(url=URL, data=data_json, headers=headers)
    print('res.json: ', res.json())

#updateData()

def delData():
    data = {'id': 10}
    data = json.dumps(data)
    res = requests.delete(url=URL, data=data, headers=headers)
    print(res.json())

#delData()
#getData(3)
#postData()
#updateData()
