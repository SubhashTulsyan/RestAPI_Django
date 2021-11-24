from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.
class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    filter_backends = [OrderingFilter]
    #ordering_fields = ['name']
    #ordering_fields = ['name', 'city']
    #ordering_fields = '__all__'