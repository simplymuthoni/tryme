from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name='parents')
    

    def __str__(self):
        return self.name