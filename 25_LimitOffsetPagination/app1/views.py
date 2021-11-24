from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 5
class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    pagination_class = MyLimitOffsetPagination