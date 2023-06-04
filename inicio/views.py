from django.shortcuts import render 

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from inicio.models import Jugador


def mi_vista(request):
    return render(request, 'inicio/inicio.html')

def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

class JugadorListView(ListView):
    model = Jugador
    template_name = "inicio/lista_jugadores.html"

class JugadorDetailView(DetailView):
    model = Jugador
    template_name = "inicio/detalle_jugador.html"


class JugadorCreateView(CreateView):
    model = Jugador
    template_name = "inicio/crear_jugador.html"
    fields = ['nombre','edad','fecha_nacimiento','posicion', 'descripcion', 'foto_de_identificacion',]
    success_url = '/jugador/'
    

class JugadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugador
    template_name = "inicio/modificar_jugador.html"
    fields = ['nombre','edad','fecha_nacimiento','posicion','descripcion', 'foto_de_identificacion',]
    success_url = '/jugador/'


class JugadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = "inicio/eliminar_jugador.html"
    success_url = '/jugador/'


