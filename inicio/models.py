from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion=RichTextField()
    fecha_nacimiento = models.DateField()
    posicion = models.CharField(max_length=20)
    foto_de_identificacion = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.posicion}"
    
