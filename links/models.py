from django.db import models
from cloudinary.models import CloudinaryField

class Links(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    link_image = CloudinaryField('image', default='placeholder')
    link_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title