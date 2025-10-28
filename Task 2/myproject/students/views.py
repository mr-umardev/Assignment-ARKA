# students/views.py

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    # queryset: Defines the data set this view will operate on (all Student objects)
    queryset = Student.objects.all() 
    
    # serializer_class: Tells the view which serializer to use for data translation
    serializer_class = StudentSerializer
    
    # The ModelViewSet automatically provides:
    # - GET /api/students/ -> list() method (to list all students)
    # - POST /api/students/ -> create() method (to add a new student)
    # - GET /api/students/{id}/ -> retrieve() method