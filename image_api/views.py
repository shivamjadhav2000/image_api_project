# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
# views.py

from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Handle the uploaded image here, save it, and return a response
        uploaded_image = request.FILES['image']
        # Implement your logic to save the image
        # You can use Django's FileField or other methods to save it to the server

        # Example response
        response_data = {
            'message': 'Image uploaded successfully',
            'image_url': 'path_to_uploaded_image.jpg',  # Replace with the actual URL
        }
        return JsonResponse(response_data)
    
    return render(request, 'upload_form.html')  # Render an HTML form for uploading images
