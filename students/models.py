from django.db import models
from parents.models import Parent

class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name