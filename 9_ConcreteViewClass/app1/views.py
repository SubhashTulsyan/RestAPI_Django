from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSer

class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    
class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer