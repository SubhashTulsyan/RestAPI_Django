from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Student
from rest_framework import serializers, validators


class StudentSer(serializers.ModelSerializer):
    def startWithr(val: str):
        if not val.lower().startswith('r'):
            raise ValidationError('not starting with r')


    #name = serializers.CharField(read_only = True)
    #name = serializers.CharField(validators = [startWithr])
    class Meta:
        model = Student
        fields = '__all__'
        #read_only_fields = ['name']
        extra_kwargs = {'name': {'read_only': True}}
    
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
        return val