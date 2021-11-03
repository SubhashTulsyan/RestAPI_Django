import json

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student(
    name="Subhash",
    age="21",
)
# a = {
#    '1':{
#        'name':'Subh',
#    },    
#    '2':{
#        'name':'Neha',
#    },    
# }

to_json_object = json.dumps(student.__dict__, indent=1)
print(to_json_object)
#print(student.__dict__)

to_python_object = json.loads(to_json_object)
print(to_python_object)
