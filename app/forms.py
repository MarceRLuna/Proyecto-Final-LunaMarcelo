
from django import forms

class Inmueble_Formulario(forms.Form):

    categoria = forms.CharField(max_length=30)
    ubicacion = forms.CharField(max_length=50)
    domitorios = forms.IntegerField()
    metros_cuadrados = forms.IntegerField()


class Inquilino_Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    mail = forms.EmailField()
    valor_alquiler = forms.IntegerField()


class Propietario_Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    mail = forms.EmailField()