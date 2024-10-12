from django.urls import path
from forum.views import crea_post, post_detalle, post_edit, post_list, borrar_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detalle, name='post_detail'),
    path('post/new/', crea_post, name='post_create'),
    path('post/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', borrar_post, name='post_delete'),
]
