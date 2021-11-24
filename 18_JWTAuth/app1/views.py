from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSer
from rest_framework_simplejwt.authentication import JWTAuthentication


# http http://127.0.0.1:8000/StudentModelViewSet/
# http http://127.0.0.1:8000/get/ username=super password=a
# http POST http://127.0.0.1:8000/refresh/ refresh=""
# http http://127.0.0.1:8000/verify/ token=""
# http http://127.0.0.1:8000/StudentModelViewSet/ 'Authorization:Bearer '<access_token>'
# http -f POST http://127.0.0.1:8000/StudentModelViewSet/ name=Subh roll=21 'Authorization:Bearer '<access_token>'
# http PUT http://127.0.0.1:8000/StudentModelViewSet/ name=Subh roll=21 'Authorization:Bearer '<access_token>'
# http DELETE http://127.0.0.1:8000/StudentModelViewSet/2 'Authorization:Bearer '<access_token>'
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer