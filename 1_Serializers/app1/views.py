from django.http.response import HttpResponse
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
import json

# Create your views here.
def student_details(request):
    # students = Student.objects.all().first()
    students = Student.objects.all()
    print("stu_dict: ", students.__dict__)
    # print('stu_dict json: ', json.dumps(students[0].__dict__))

    # ser_data = StudentSerializers(students)
    ser_data = StudentSerializers(students, many=True)
    print("ser_data: ", ser_data)
    print("ser_data.data: ", ser_data.data)

    ser_data_json = JSONRenderer().render(ser_data.data)
    print("ser_data_json: ", ser_data_json)
    return HttpResponse(ser_data_json, content_type="application/json")
    # return JsonResponse(ser_data.data, safe=False)
