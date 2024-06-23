from django.contrib import admin
from .models import Inmueble, Propietario, Inquilino

# Register your models here.

admin.site.register(Inmueble)
admin.site.register(Inquilino)
admin.site.register(Propietario)