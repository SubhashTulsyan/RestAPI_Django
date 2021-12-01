from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    #url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    