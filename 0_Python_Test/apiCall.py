import requests

URL = 'http://127.0.0.1:8000/api/students/'

res = requests.get(url=URL)

print(res.json())

# import json

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student = Student(
#     name="Subhash",
#     age="21",
# )

# to_json_object = json.dumps(student.__dict__, indent=1)
# print('to_json_object: ', type(to_json_object))
# #print(student.__dict__)

# to_python_object = json.loads(to_json_object)
# print('to_python_object: ', type(to_python_object))
