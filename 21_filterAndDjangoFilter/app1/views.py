from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    #queryset = Student.objects.filter(id = 1)
    serializer_class = StudentSer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    # #dummy
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(user = user)