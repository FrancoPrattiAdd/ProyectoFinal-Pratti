from django.urls import path
from .views import lista_msj, enviar_msj, borrar_msj

urlpatterns = [
    path('', lista_msj, name='message_list'), 
    path('create/', enviar_msj, name='message_create'),  
    path('delete/<int:pk>/', borrar_msj, name='message_delete'),  
]
