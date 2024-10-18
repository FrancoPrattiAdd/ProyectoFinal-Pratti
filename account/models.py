from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuario simple, extendiendo de AbstractUser
class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 

    def __str__(self):
        return self.username 
