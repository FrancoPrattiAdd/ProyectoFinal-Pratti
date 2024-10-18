from django import forms
from .models import Producto

# Formulario para crear y editar productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen'] 

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre del producto'})
        self.fields['precio'].widget.attrs.update({'placeholder': 'Precio del producto'})
