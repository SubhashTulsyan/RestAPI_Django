from sys import implementation
from django.http.response import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSer
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# @csrf_exempt
# def home(request):
#     # if request.method == "POST":

#     # print("in POST")
#     # data = request.body
#     # print("data: ", data)
#     data = {
#         "name": "Nidhi",
#         "roll": 3211,
#     }
#     data = json.dumps(data)
#     print("data: ", type(data))
#     stream_data = io.BytesIO(data)
#     print("stream_data: ", stream_data)

#     parsed_data = JSONParser().parse(stream_data)
#     print("parsed_data: ", parsed_data)

#     stuDeser = StudentSer(data=parsed_data)
#     print("stuDeser: ", stuDeser)

#     if stuDeser.is_valid():
#         stuDeser.save()
#         res = {"msg": "Data Created"}
#         # json_res = JSONRenderer().render(res)
#         # return HttpResponse(json_res, content_type='application/json')
#         return JsonResponse(res)

#         # validated_data = stuDeser.validated_data
#         # print('validated_data: ', validated_data)
#     else:

#         # json_res = JSONRenderer().render(stuDeser.errors)
#         # return HttpResponse(json_res, content_type='application/json')
#         return JsonResponse(stuDeser.errors)


@csrf_exempt
def home(request):
    if request.method == "POST":
        print("in POST")
        data = request.body
        print("data: ", data)
        stream_data = io.BytesIO(data)
        print("stream_data: ", stream_data)

        parsed_data = JSONParser().parse(stream_data)
        print("parsed_data: ", parsed_data)

        stuDeser = StudentSer(data=parsed_data)
        print("stuDeser: ", stuDeser)

        if stuDeser.is_valid():
            stuDeser.save()
            res = {"msg": "Data Created"}
            # json_res = JSONRenderer().render(res)
            # return HttpResponse(json_res, content_type='application/json')
            return JsonResponse(res)

            # validated_data = stuDeser.validated_data
            # print('validated_data: ', validated_data)
        else:

            # json_res = JSONRenderer().render(stuDeser.errors)
            # return HttpResponse(json_res, content_type='application/json')
            return JsonResponse(stuDeser.errors)
