from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm
from .models import Message

def lista_msj(request):
    messages = Message.objects.all() 
    return render(request, 'mensajeria/lista_msj.html', {'messages': messages})

def enviar_msj(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('message_list') 
    else:
        form = MessageForm()
    return render(request, 'mensajeria/mensaje_nuevo.html', {'form': form})

def borrar_msj(request, pk):
    message = get_object_or_404(Message, pk=pk) 
    if request.method == 'POST':
        message.delete() 
        return redirect('message_list')  
    return render(request, 'mensajeria/borrar_msj.html', {'message': message})
