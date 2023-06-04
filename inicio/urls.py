from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('sobre_nosotros', views.sobre_nosotros, name='sobre_nosotros'),
    path('/inicio/jugador/', views.JugadorListView.as_view, name='lista_jugadores'),
    path('/inicio/jugador/crear/', views.JugadorCreateView.as_view, name='crear_jugador'),
    path('/inicio/jugador/<int:pk>/', views.JugadorDetailView.as_view, name='detalle_jugador'),
    path('/inicio/jugador/<int:pk>/modificar/', views.JugadorUpdateView.as_view, name='modificar_jugador'),
    path('/inicio/jugador/<int:pk>/eliminar/', views.JugadorDeleteView.as_view, name='eliminar_jugador'),


]
