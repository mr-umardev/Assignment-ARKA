# myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add this line to map all URLs from students/urls.py to the /api/ path
    path('api/', include('students.urls')), 
]