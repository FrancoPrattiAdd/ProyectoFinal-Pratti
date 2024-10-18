from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, CarritoProducto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Vista para listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()  
    return render(request, 'products/listar_productos.html', {'productos': productos})

# Vista para agregar un nuevo producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('listar_productos')  
    else:
        form = ProductoForm()  
    return render(request, 'products/agregar_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)  
        if form.is_valid():
            form.save()  
            return redirect('listar_productos') 
    else:
        form = ProductoForm(instance=producto) 
    return render(request, 'products/editar_producto.html', {'form': form})

# Vista para manejar el carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    carrito_producto.cantidad += 1
    carrito_producto.save()

    return redirect('listar_productos')


@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    total_price = sum(item.cantidad * item.producto.precio for item in carrito.carritoproducto_set.all())
    return render(request, 'products/ver_carrito.html', {'carrito': carrito, 'total_price': total_price})

def eliminar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto__id=producto_id)

    carrito_producto.delete() 

    return redirect('ver_carrito')

