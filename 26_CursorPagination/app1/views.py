from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSer
from rest_framework.pagination import CursorPagination
# Create your views here.
class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 3
    ordering = '-id'
    page_size_query_param = 'pg'
    max_page_size = 4
    offset_cutoff = 1000

class Stuapi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    pagination_class = MyCursorPagination