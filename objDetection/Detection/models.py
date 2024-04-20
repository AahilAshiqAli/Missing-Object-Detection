from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class User(AbstractUser):
    pass

class Object(models.Model):
    user = models.ForeignKey(User, related_name='detection_objects', on_delete=models.CASCADE)
    image_location = models.ImageField(upload_to=settings.STATIC_URL + 'object_images/')

    def __str__(self):
        return f"Object for {self.user.username}"
