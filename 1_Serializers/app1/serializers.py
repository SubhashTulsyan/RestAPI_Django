from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    # sec = (
    #     ('-1', '--Select--'),
    #     ('1', 'A'),
    #     ('2', 'B'),
    #     ('3', 'C'),
    #     ('4', 'D'),
    # )
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=80)
    age = serializers.IntegerField()
    #section = serializers.CharField(max_length=100, choices=sec, default=-1)
    section = serializers.CharField(max_length=100)