from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .models import Student
from .serializers import StudentSer
from .custompermissions import Customperm

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Customperm]
    
    

# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer