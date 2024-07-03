from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('informesSectoriales/', InformesSectoriales, name="informesSectoriales"),
    path('prensa', prensa, name="prensa"),
    path('quienesSomos', quienesSomos, name="quienesSomos"),
    path('clienteForm', clientesForm, name="clienteForm"),
    path('prensaForm', PrensaForm, name="prensaForm"),
    path('informesSectorialesForm', InformesForm, name="informesSectorialesForm"),
    path('buscarClientes', buscarClientes, name="buscarClientes"),
    path('encontrarClientes', encontrarClientes, name="encontrarClientes"),
    ]
