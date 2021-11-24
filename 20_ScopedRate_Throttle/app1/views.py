from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .throttles import MyThrottle
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # throttle_class = [AnonRateThrottle, UserRateThrottle]
#     throttle_class = [AnonRateThrottle, MyThrottle]

class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    throttle_class = [ScopedRateThrottle]
    throttle_scope = 'lc'

    
class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    throttle_class = [ScopedRateThrottle]
    throttle_scope = 'rud'
    
# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer