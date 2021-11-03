from django.db import models

# Create your models here.
class Student(models.Model):
    sec = (
        ('-1', '--Select--'),
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
        ('4', 'D'),
    )
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    section = models.CharField(max_length=100, choices=sec, default=-1)