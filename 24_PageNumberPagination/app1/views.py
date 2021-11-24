from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class MyPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'rec'
    max_page_size = 4
    last_page_strings = 'end'

class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    pagination_class = MyPagination