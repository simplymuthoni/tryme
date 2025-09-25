from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def create_with_parents(cls, name, admission_number, parents_data):
        """
        Create a student and associate with parents in one operation.
        
        parents_data: list of dicts with parent info
        Example: [{'name': 'John Doe', 'phone': '123456789'}, ...]
        """
        from parents.models import Parent
        
        # Create the student
        student = cls.objects.create(name=name, admission_number=admission_number)
        
        # Create or get parents and associate them
        parent_objects = []
        for parent_data in parents_data:
            parent, created = Parent.objects.get_or_create(
                name=parent_data['name'],
                phone=parent_data['phone']
            )
            parent_objects.append(parent)
        
        # Use set() to add all parents at once (no loop needed)
        student.parents.set(parent_objects)
        
        return student
    
    def add_parents(self, parents_data):
        """Add multiple parents to existing student"""
        from parents.models import Parent
        
        parent_objects = []
        for parent_data in parents_data:
            parent, created = Parent.objects.get_or_create(
                name=parent_data['name'],
                phone=parent_data['phone']
            )
            parent_objects.append(parent)
        
        # Add parents without removing existing ones
        self.parents.add(*parent_objects)
