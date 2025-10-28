# students/serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # ModelSerializer is a shortcut to automatically generate fields
    # corresponding to the model fields.
    class Meta:
        model = Student
        # The 'id' is necessary to uniquely identify students (auto-created by Django)
        fields = ['id', 'name', 'age', 'email'] 
        # Alternatively, use fields = '__all__' to include all model fields