from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ImageViewSet
from . import views

router = SimpleRouter()
router.register(r'upload', ImageViewSet)

urlpatterns = [
    # Include the API URL patterns defined using the router
    path('', include(router.urls)),
    
    # Add app-specific URL patterns here
    path('upload/', views.upload_image, name='upload_image'),
    # ...
]
