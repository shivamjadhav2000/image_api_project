# image_api/models.py
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
