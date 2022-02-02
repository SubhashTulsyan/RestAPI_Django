from functools import partial
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSer


class Student_VS(viewsets.ViewSet):
    def list(self, request):
        print("********list***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        students = Student.objects.all()
        ser = StudentSer(students, many=True)
        return Response(ser.data)

    def create(self, request):
        print("********Create***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        ser = StudentSer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response({"msg": "Data Created"})

    def retrieve(self, request, pk=None):
        print("********Retrieve***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        student = Student.objects.get(id=pk)
        ser = StudentSer(student)
        return Response(ser.data)

    def update(self, request, pk=None):
        print("********Update***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        student = Student.objects.get(id=pk)
        ser = StudentSer(student, data=request.data, partial=False)
        if ser.is_valid():
            ser.save()
        return Response({"msg": "Data Updated"})

    def partial_update(self, request, pk=None):
        print("********Partial Update***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        student = Student.objects.get(id=pk)
        ser = StudentSer(student, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
        return Response({"msg": "Data Updated partial"})

    def destroy(self, request, pk=None):
        print("********Destroy***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({"msg": "Data Deleted"})
