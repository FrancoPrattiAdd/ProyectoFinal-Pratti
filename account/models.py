from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
