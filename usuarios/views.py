from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import FormularioRegistro, EdicionPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def login(request):
    
    if request.method == 'POST':
        fromulario = AuthenticationForm(request, data=request.POST)
        
        if fromulario.is_valid():
            usuario = fromulario.cleaned_data.get('username')
            clave = fromulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=clave)
            
            login_django(request, user)
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            
           return render(request, 'usuarios/login.html', {'from': fromulario})
    
    fromulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'from': fromulario})


def registro(request):
       
    if request.method == 'POST':
        fromulario = FormularioRegistro(request.POST)
        
        if fromulario.is_valid():
            fromulario.save()

            return redirect('usuarios:login')
        else:
            
           return render(request, 'usuarios/registro.html', {'from': fromulario})
    
    fromulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'from': fromulario})

@login_required
def editar_perfil(request):


    if request.method == 'POST':
        fromulario = EdicionPerfil(request.POST, request.FILES,  instance=request.user)
        
        if fromulario.is_valid():
            
            if fromulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = fromulario.cleaned_data.get('avatar')
                request.user.infoextra.save()
            
            fromulario.save()

            return redirect('usuarios:editar_perfil')
        else:
            
           return render(request, 'usuarios/editar_perfil.html', {'from': fromulario})
    
    fromulario = EdicionPerfil(initial={'avatar': request.user.infoextra.avatar}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'from': fromulario})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_clave.html'
    success_url = reverse_lazy('usuarios:editar_perfil')