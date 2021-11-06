from functools import partial
from django.http.response import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentAPI_CRUD(request, pk = None):
    if request.method == 'GET':
        data = request.data
        print('request.data: ', data)
        id = pk
        if id is not None:
            student = Student.objects.get(id = id)
            studer_ser = StudentSer(student)
            return Response(studer_ser.data)
        else:
            students = Student.objects.all()
            students_ser = StudentSer(students, many = True)
            return Response(students_ser.data)

    if request.method == 'POST':
        data = request.data
        print('post data: ', data)
        
        stuser = StudentSer(data=data)
        if stuser.is_valid():
            stuser.save()
            msg = {
                'msg': 'Data Created'
            }
            return Response(msg, status = status.HTTP_201_CREATED)
        else:
            return Response(stuser.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data
        print('put data: ', data)

        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stuser = StudentSer(stu, data=data, partial = False)
            if stuser.is_valid():
                stuser.save()
                msg = {
                    'msg': 'Data Updated'
                }
                return Response(msg)
            else:
                return Response({'msg': 'Some issue'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'ID not found'}, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        data = request.data
        print('put data: ', data)

        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stuser = StudentSer(stu, data=data, partial = True)
            if stuser.is_valid():
                stuser.save()
                msg = {
                    'msg': 'Data Updated'
                }
                return Response(msg)
            else:
                return Response({'msg': 'Some issue'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'ID not found'}, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data = request.data
        print('delete data: ', data)

        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            msg = {
                    'msg': 'Data Deleted'
                    }
            return Response(msg)
        else:
            return Response({'msg': 'ID not found'}, status = status.HTTP_400_BAD_REQUEST)