from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    empresa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido} , {self.empresa}"

class InformeSectorial(models.Model):
    sector = models.CharField(max_length=50)
    informesDisponibles = models.BooleanField()
    UltimaPublicacion = models.DateField()

    def __str__(self):
        return f"{self.sector} , {self.UltimaPublicacion}"
    
   
class Prensa(models.Model):
    TituloNoticia = models.CharField(max_length=50)
    medio = models.CharField(max_length=50)
    LinkNoticia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medio} , {self.LinkNoticia}"
