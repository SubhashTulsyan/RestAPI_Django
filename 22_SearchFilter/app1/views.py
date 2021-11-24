from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.
class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    #queryset = Student.objects.filter(id = 1)
    serializer_class = StudentSer
    #filter_backends = [SearchFilter, DjangoFilterBackend]
    #filter_fields = ['city']
    filter_backends = [SearchFilter]
    search_fields = ['$name']
    # search_fields = ['^name'] # starts with
    # search_fields = ['=name'] # exact
    # search_fields = ['@name'] # full text search (POSTGRES supported)
    # search_fields = ['$name'] # Regex search

    # for settings.py
    # REST_FRAMEWORK = {
    #     'DEFAULT_FILTER_BACKENDS':
    #     ['django_filters.rest_framework.DjangoFilterBackend']
    # }
    # REST_FRAMEWORK = {
    #     'SEARCH_PARAM': 'st'
    # }

    #search_fields = ['name', 'roll']    

    # #dummy
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(user = user)