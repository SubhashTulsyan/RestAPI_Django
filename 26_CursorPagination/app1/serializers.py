from django.db.models import fields
from .models import Student
from rest_framework import serializers
class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
