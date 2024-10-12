from django.db import models

class Message(models.Model):
    emisor = models.CharField(max_length=255) 
    receptor = models.EmailField()
    body = models.TextField(default='No hay contenido') 
    enviado_el = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Mensaje de {self.emisor} a {self.receptor}: {self.body[:50]}...'  
