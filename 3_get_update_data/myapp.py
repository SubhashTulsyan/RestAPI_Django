import requests, json


URL = 'http://127.0.0.1:8000/getData/'
def getData(id = None):
    print('id: ', id)
    a = {}
    if id is not None:
        a = {
            'id': id,
        }
    js_data = json.dumps(a)
    print('js_data: ', js_data)

    r = requests.get(url=URL, data = js_data)
    print('r: ', r)
    print('r json: ', r.json())

def postData():
    data = {
        'name': 'Aqku',
        'roll': '122',
    }

    res = requests.post(url=URL, data=json.dumps(data))
    print(res.json())
#postData()

def updateData():
    data = {
        'id': 12,
        'name': 'Raj',
    }
    data_json = json.dumps(data)
    res = requests.put(url=URL, data=data_json)
    print('res.json: ', res.json())

#updateData()

def delData():
    data = {'id': 1}
    data = json.dumps(data)
    res = requests.delete(url=URL, data=data)
    print(res.json())

#delData()
#getData(11)
postData()
