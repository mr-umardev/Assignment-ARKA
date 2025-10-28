# students/urls.py

from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
# This registers the ViewSet, making the /students/ path available relative to the parent URL
router.register(r'students', StudentViewSet, basename='student') 

urlpatterns = router.urls