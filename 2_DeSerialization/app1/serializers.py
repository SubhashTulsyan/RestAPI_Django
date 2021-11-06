from .models import Student
from rest_framework import serializers
class StudentSer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.save()
    #     return instance