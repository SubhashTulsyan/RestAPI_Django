from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser\
    , IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .models import Student
from .serializers import StudentSer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    #http http://127.0.0.1:8000/StudentModelViewSet/ 'Authorization:Token 13997216e12394d1cc28d979c3c77ef95ce1b460'
    #http -f POST http://127.0.0.1:8000/StudentModelViewSet/ name=Subh roll=22 'Authorization:Token 13997216e12394d1cc28d979c3c77ef95ce1b460'
    #http PUT http://127.0.0.1:8000/StudentModelViewSet/4/ name=Subh roll=22 'Authorization:Token 13997216e12394d1cc28d979c3c77ef95ce1b460'
    #http DELETE http://127.0.0.1:8000/StudentModelViewSet/4/ 'Authorization:Token 13997216e12394d1cc28d979c3c77ef95ce1b460'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer