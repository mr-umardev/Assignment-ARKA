# students/models.py

from django.db import models

class Student(models.Model):
    # CharField is used for short-to-medium length strings
    name = models.CharField(max_length=100) 
    
    # IntegerField is used for whole numbers like age
    age = models.IntegerField()
    
    # EmailField validates the input as an email address
    # unique=True prevents duplicate email entries
    email = models.EmailField(unique=True) 

    def __str__(self):
        # A human-readable representation, useful in the Django Admin
        return self.name