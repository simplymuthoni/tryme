from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

from .models import (Student)
from .serializers import (StudentSerializer)

@method_decorator(csrf_exempt, name='dispatch')
class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Any extra handling for applications (e.g., send email, log data)
        serializer.save()

    def create(self, request, *args, **kwargs):
        print("DATA RECEIVED:", request.data)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("ERRORS:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    



