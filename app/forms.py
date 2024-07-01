
from django import forms
from .models import Propietario, Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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


# class Propietario_Formulario(forms.Form):
#     nombre = forms.CharField(max_length=30)
#     apellido = forms.CharField(max_length=30)
#     telefono = forms.IntegerField()
#     mail = forms.EmailField()

class Propietario_Formulario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ('__all__')


# Modificación para el formulario de edición del perfil de usuario

class UserEditForm (UserChangeForm):

    password = forms.CharField(
        help_text='',
        widget=forms.HiddenInput, required=False
    )

    password_1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # creamos nuestra propia validación dentro del formulario para el caso de las contraseñas
    def clean_password_2(self): 
        # el parámetro self es una instancia de nuesto formulario UserEditForm, por lo tanto contiene la data guardada en en la variable password
        psw_1 = self.cleaned_data['password_1']
        psw_2 = self.cleaned_data['password_2'] # recuperamos los datos cargados por el user en los campos de password_1 y password_2

        if psw_1 != psw_2:
            raise forms.ValidationError('Error, las contraseñas no coinciden')
        return psw_2


class Avatar_Formulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('imagen', )








