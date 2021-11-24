from rest_framework import serializers
from .models import Student
class StudentSer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='student-detail')
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'age']
        #fields = ['id', 'name', 'age']

        # extra_kwargs = {
        #     'url': {'view_name': 'student-detai', 'lookup_field': 'id'},
        #     #'users': {'lookup_field': 'username'}
        # }