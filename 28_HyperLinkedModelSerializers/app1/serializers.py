from rest_framework import serializers
from .models import Student
class StudentSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url','id', 'name', 'age')