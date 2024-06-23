
from django.urls import path
# desde el archivo views en la carpeta de la aplicación importamos todas las funciones que ejecutaremos al ingresar a las urls
from app.views import inicio, inmueble_formulario, inquilino_formulario, propietario_formulario, busqueda_inmueble, buscar, lista_inmuebles, eliminar_inmueble, editar_inmueble 

urlpatterns = [
    path('', inicio, name="inicio"),    
    path('inmueble-formulario/', inmueble_formulario, name='inmueble_formulario'),
    path('inquilino-formulario/', inquilino_formulario, name='inquilino_formulario'),
    path('propietario-formulario/', propietario_formulario, name='propietario_formulario'),
    path('busqueda-inmueble/', busqueda_inmueble, name='busqueda_inmueble'), # endpoint que denominamos "busqueda-inmueble/" que invoca a la función "busqueda_inmueble"
    path('buscar/', buscar, name='buscar_inmueble'), # endpoint que tiene la función "buscar" y que se invoca cuando el formulario del template "busqueda_inmueble.html" se submitea.
    path('lista-inmuebles/', lista_inmuebles, name='lista_inmuebles'),
    path('eliminar-inmuebles/<int:id>', eliminar_inmueble, name='eliminar_inmuebles'),
    path('editar-inmuebles/<int:id>', editar_inmueble, name='editar_inmuebles'),
]
