from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    students = models.ManyToManyField('students.Student', related_name='parents')
   
    def __str__(self):
        return self.name
    
