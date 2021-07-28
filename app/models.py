from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to ="myphotos")
    description = models.CharField(null=True , blank=False , max_length=40)
    tags = TaggableManager()
    

    def __str__(self):
        return self.description

    
