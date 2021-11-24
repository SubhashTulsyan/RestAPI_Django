from rest_framework import viewsets
from .models import Student
from .serializers import StudentSer
# Create your views here.
class PlayerAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer