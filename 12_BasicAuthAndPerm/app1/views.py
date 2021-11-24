from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Student
from .serializers import StudentSer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    authentication_classes = [BasicAuthentication]
    #permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]
    #Defined globally in settings.py
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]



# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer