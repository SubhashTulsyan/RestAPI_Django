from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSer
import io
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def studentAPI_CRUD(request):
    if request.method == 'GET':
        data = request.data
        print('request.data: ', data)
        id = data.get('id', None)
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
            return Response(msg)
        else:
            return Response({'msg': 'Some issue'}, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        data = request.data
        print('put data: ', data)

        id = data.get('id', None)
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

        id = data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            msg = {
                    'msg': 'Data Deleted'
                    }
            return Response(msg)
        else:
            return Response({'msg': 'ID not found'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def StudentAPI(request):
    if request.method == 'GET':
        json_data = request.body
        print('request.body: ', json_data)

        streamed_data = io.BytesIO(json_data)
        print('streamed_data: ', streamed_data)

        pythonData = JSONParser().parse(streamed_data)
        print('pythonData: ', pythonData)

        id = pythonData.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            print('stu_id: ', stu)
            stuser = StudentSer(stu)
            print('stuser_id: ', stuser)
        else:
            stu = Student.objects.all()
            print('stu', stu)
            stuser = StudentSer(stu, many = True)
            print('stuser', stuser)
        return Response(stuser.data)

    if request.method == 'POST':
        data = request.body
        print('request.body: ', data)

        streamed_data = io.BytesIO(data)
        print('streamed_data: ', streamed_data)

        pythonData = JSONParser().parse(streamed_data)
        print('pythonData: ', pythonData)

        stuser = StudentSer(data = pythonData)
        print('stuser: ', stuser)
        if stuser.is_valid():
            stuser.save()
            res = {'msg': 'Data Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(stuser.errors, status= status.HTTP_400_BAD_REQUEST)

            

    if request.method == 'PUT':
        json_data = request.body
        print('json_data: ', json_data)

        streamed_data = io.BytesIO(json_data)
        print('streamed_data: ', streamed_data)

        parsed_data = JSONParser().parse(streamed_data)
        print('parsed_data: ', parsed_data)
        
        id = parsed_data.get('id')
        stu = Student.objects.get(id = id)
        ser = StudentSer(stu, data = parsed_data, partial = True)

        if ser.is_valid():
            ser.save()
            msg = {'msg': 'Updated'}
            return Response(msg)
            # msg = JSONRenderer().render(msg)
            # return HttpResponse(msg, 'application/json')
        #return HttpResponse(ser.errors, 'application/json')
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data = request.body
        print('req.body: ', data)
        streamed_data = io.BytesIO(data)
        parsed_data = JSONParser().parse(streamed_data)
        id = parsed_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        msg = {'msg': 'Data Deleted'}
        return Response(msg)
        # msg = JSONRenderer().render(msg)
        # return HttpResponse(msg, 'application/json')