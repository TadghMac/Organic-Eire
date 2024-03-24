from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Links(models.Model):
    title = models.CharField(max_length=200)
    link_image = CloudinaryField('image', default='placeholder')
    link_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title