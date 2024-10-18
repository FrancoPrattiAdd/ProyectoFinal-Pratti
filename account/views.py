from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm

# Vista para registrar un nuevo usuario
def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  
            return redirect('perfil')  
    else:
        form = RegistroForm()
    return render(request, 'account/registro.html', {'form': form})

# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)  # Verifica las credenciales
        if usuario is not None:
            login(request, usuario)  # Inicia sesión al usuario
            return redirect('perfil')  # Redirige al perfil
        else:
            # Agrega un mensaje de error si las credenciales son incorrectas
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'account/iniciar_sesion.html', {'error_message': error_message})
    return render(request, 'account/iniciar_sesion.html')

# Vista para ver el perfil del usuario
@login_required
def perfil(request):
    return render(request, 'account/perfil.html', {'usuario': request.user})

# Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil') 
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'account/editar_perfil.html', {'form': form})
