from django.shortcuts import render
from entidades.models import *
from entidades.forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def clientes(request):
    contexto = {"Cliente" : Cliente.objects.all()}
    return render(request, "entidades/clientes.html", contexto)

def InformesSectoriales(request):
    contexto = {"informesSectoriales" : InformeSectorial.objects.all()}
    return render(request, "entidades/InformesSectoriales.html", contexto)

def prensa(request):
    contexto = {"prensa" : Prensa.objects.all()}
    return render(request, "entidades/prensa.html", contexto)

def quienesSomos(request):
    return render(request, "entidades/quienesSomos.html")


def clientesForm(request):
    if request.method == "POST":
        miForm = clienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_empresa = miForm.cleaned_data.get("empresa")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido,email=cliente_email,empresa=cliente_empresa,)
            cliente.save()
            contexto = {"Cliente" : Cliente.objects.all()}
            return render(request, "entidades/clientes.html", contexto)
    else:   
        miForm = clienteForm()

    return render(request, "entidades/clienteForm.html", {"form" :  miForm}) 


def PrensaForm(request):
    if request.method == "POST":
        miForm = prensaForm(request.POST)
        if miForm.is_valid():
            prensa_noticia = miForm.cleaned_data.get("TituloNoticia")
            prensa_medio = miForm.cleaned_data.get("medio")
            prensa_link = miForm.cleaned_data.get("LinkNoticia")
            prensa = Prensa(TituloNoticia=prensa_noticia, medio=prensa_medio,LinkNoticia=prensa_link)
            prensa.save()
            contexto = {"prensa" : Prensa.objects.all()}
            return render(request, "entidades/prensa.html", contexto)
    else:   
        miForm = prensaForm()

    return render(request, "entidades/prensaForm.html", {"form" :  miForm}) 

def InformesForm(request):
    if request.method == "POST":
        miForm = informesForm(request.POST)
        if miForm.is_valid():
            informes_sector = miForm.cleaned_data.get("sector")
            informes_disponible = miForm.cleaned_data.get("informesDisponibles")
            informes_fecha = miForm.cleaned_data.get("UltimaPublicacion")
            informes = InformeSectorial(sector=informes_sector, informesDisponibles=informes_disponible,UltimaPublicacion=informes_fecha)
            informes.save()
            contexto = {"informesSectoriales" : InformeSectorial.objects.all()}
            return render(request, "entidades/InformesSectoriales.html", contexto)
    else:   
        miForm = informesForm()

    return render(request, "entidades/informesSectorialesForm.html", {"form" :  miForm}) 

def buscarClientes(request):
    return render(request, "entidades/buscarClientes.html")


def encontrarClientes(request):
    if request.GET["Buscar"]:
        patron= request.GET["Buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {"clientes" : clientes}
    else:
        contexto = {"clientes" : Cliente.objects.all()}
    return render(request, "entidades/clientes.html", contexto)