from .models import Student
from .serializers import StudentSer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class classapiview(APIView):
    def get(self,request, pk = None, format = None):
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

    def post(self, request, format = None):
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

    def put(self, request, pk, format=None):
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
    def patch(self, request, pk, format=None):
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
    def delete(self, request, pk, format = None):
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