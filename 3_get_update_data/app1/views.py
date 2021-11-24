from django.http.response import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
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
        return JsonResponse(stuser.data, safe=False)

    def post(self, request, *args, **kwargs):
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
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type = 'application/json')
        json_res = JSONRenderer().render(stuser.errors)
        return HttpResponse(json_res, content_type = 'application/json')

    def put(self, request, *args, **kwargs):
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
            msg = JSONRenderer().render(msg)
            return HttpResponse(msg, 'application/json')
        return HttpResponse(ser.errors, 'application/json')
        
    def delete(self, request, *args, **kwargs):
        data = request.body
        print('req.body: ', data)
        streamed_data = io.BytesIO(data)
        parsed_data = JSONParser().parse(streamed_data)
        id = parsed_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        msg = {'msg': 'Data Deleted'}
        msg = JSONRenderer().render(msg)
        return HttpResponse(msg, 'application/json')

# @csrf_exempt
# def getData(request):
#     if request.method == 'GET':
#         json_data = request.body
#         print('request.body: ', json_data)

#         streamed_data = io.BytesIO(json_data)
#         print('streamed_data: ', streamed_data)

#         pythonData = JSONParser().parse(streamed_data)
#         print('pythonData: ', pythonData)

#         id = pythonData.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             print('stu_id: ', stu)
#             stuser = StudentSer(stu)
#             print('stuser_id: ', stuser)
#         else:
#             stu = Student.objects.all()
#             print('stu', stu)
#             stuser = StudentSer(stu, many = True)
#             print('stuser', stuser)
#         # json_data = JSONRenderer().render(stuser.data)
#         # print('json_data', json_data)
#         return JsonResponse(stuser.data, safe=False)

#     if request.method == 'POST':
#         data = request.body
#         print('request.body: ', data)

#         streamed_data = io.BytesIO(data)
#         print('streamed_data: ', streamed_data)

#         pythonData = JSONParser().parse(streamed_data)
#         print('pythonData: ', pythonData)

#         stuser = StudentSer(data = pythonData)
#         print('stuser: ', stuser)
        
#         if stuser.is_valid():
#             stuser.save()
#             res = {'msg': 'Data Created'}
#             json_res = JSONRenderer().render(res)
#             return HttpResponse(json_res, content_type = 'application/json')
#         json_res = JSONRenderer().render(stuser.errors)
#         return HttpResponse(json_res, content_type = 'application/json')

#     if request.method == 'PUT':
#         json_data = request.body
#         print('json_data: ', json_data)

#         streamed_data = io.BytesIO(json_data)
#         print('streamed_data: ', streamed_data)

#         parsed_data = JSONParser().parse(streamed_data)
#         print('parsed_data: ', parsed_data)
        
#         id = parsed_data.get('id')
#         stu = Student.objects.get(id = id)
#         ser = StudentSer(stu, data = parsed_data, partial = True)

#         if ser.is_valid():
#             ser.save()
#             msg = {'msg': 'Updated'}
#             msg = JSONRenderer().render(msg)
#             return HttpResponse(msg, 'application/json')
#         return HttpResponse(ser.errors, 'application/json')
        
#     if request.method == 'DELETE':
#         data = request.body
#         print('req.body: ', data)
#         streamed_data = io.BytesIO(data)
#         parsed_data = JSONParser().parse(streamed_data)
#         id = parsed_data.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         msg = {'msg': 'Data Deleted'}
#         msg = JSONRenderer().render(msg)
#         return HttpResponse(msg, 'application/json')




        

