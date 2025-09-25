from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # Remove the ManyToManyField from here to avoid circular import
    # The relationship is defined in Student model
    
    def __str__(self):
        return self.name
    
    @classmethod
    def create_with_students(cls, name, phone, students_data):
        """
        Create a parent and associate with students.
        
        students_data: list of dicts with student info
        Example: [{'name': 'Jane Smith', 'admission_number': 'ADM001'}, ...]
        """
        from students.models import Student
        
        # Create the parent
        parent = cls.objects.create(name=name, phone=phone)
        
        # Create or get students and associate them
        student_objects = []
        for student_data in students_data:
            student, created = Student.objects.get_or_create(
                admission_number=student_data['admission_number'],
                defaults={'name': student_data['name']}
            )
            student_objects.append(student)
        
        # Add this parent to all students at once
        for student in student_objects:
            student.parents.add(parent)
        
        return parent
