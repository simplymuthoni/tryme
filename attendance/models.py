from django.db import models

class Attendance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('absent', 'Absent')]
    )

    def __str__(self):
        return f"{self.student.name} ({self.student.admission_number}) - {self.date} - {self.status}"

    @property
    def student_name(self):
        return self.student.name

    @property
    def admission_number(self):
        return self.student.admission_number

    @property
    def parents(self):
        """Return all parents linked to this student."""
        return [parent.name for parent in self.student.parents.all()]

    @property
    def parent_contacts(self):
        """Return all parent phone numbers for this student."""
        return [parent.phone for parent in self.student.parents.all()]
