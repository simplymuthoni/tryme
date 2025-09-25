from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (StudentViewSet)

# Create router instance for automatic URL pattern generation
router = DefaultRouter()

# Register ViewSets with the router
router.register(r'students', StudentViewSet)

# URL patterns for the academics app
urlpatterns = [
    path('', include(router.urls)),
]
