from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSer

# Don't required PK.
class LCStudentData(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

## PK is required.
class RUDStudentData(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class StudentData(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
# class StudentDel(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
