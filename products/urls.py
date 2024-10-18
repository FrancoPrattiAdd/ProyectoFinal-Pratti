from django.urls import path
from .views import listar_productos, agregar_producto, editar_producto, agregar_al_carrito, ver_carrito, eliminar_del_carrito

urlpatterns = [
    path('', listar_productos, name='listar_productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]
