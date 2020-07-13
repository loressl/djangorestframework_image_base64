from django.db import models

# Create your models here.   
class Image_Base64(models.Model):
    image= models.TextField()
    
    def __str__(self):
        return self.image
