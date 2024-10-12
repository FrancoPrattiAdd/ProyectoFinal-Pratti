from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, ProfileForm
from .models import Usuario

# Vista de Registro
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) 
            login(request, user)  
            return redirect('profile')  
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Vista de Inicio de Sesión
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Vista de Cerrar Sesión
def user_logout(request):
    logout(request)
    return redirect('login')

# Vista del Perfil
@login_required
def profile(request):
    usuario = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save() 
            return redirect('profile')
    else:
        form = ProfileForm(instance=usuario)
    return render(request, 'accounts/profile.html', {'form': form})
