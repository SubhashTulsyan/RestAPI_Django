from django.core.exceptions import ValidationError
from .models import Student
from rest_framework import serializers, validators


def startWithr(val: str):
    if not val.lower().startswith('r'):
        raise ValidationError('not starting with r')

class StudentSer(serializers.Serializer):

    name = serializers.CharField(max_length=100, validators = [startWithr])
    roll = serializers.IntegerField()

    # Object level validation
    def validate(self, attrs):
        nm = attrs.get('name')
        roll = attrs.get('roll')
        if nm is not 'rocky' and roll is not 155:
            raise serializers.ValidationError('rocky155error')
        return attrs

    # Field level validation
    def validate_roll(self, val):
        if val>1000:
            raise serializers.ValidationError('Please Enter a number less than or equal to 1000')
            
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.save()
        return instance