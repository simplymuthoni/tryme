from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    