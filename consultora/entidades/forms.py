from django import forms

class clienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=50, required=True)
    empresa = forms.CharField(max_length=50, required=True)

class prensaForm(forms.Form):
    TituloNoticia = forms.CharField(max_length=50, required=True)
    medio = forms.CharField(max_length=50, required=True)
    LinkNoticia = forms.CharField(max_length=50, required=True)

class informesForm(forms.Form):
    sector = forms.CharField(max_length=50, required=True)
    informesDisponibles = forms.BooleanField(required=True)
    UltimaPublicacion = forms.DateField(required=True)