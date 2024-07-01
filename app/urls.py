
from django.urls import path
# desde el archivo views en la carpeta de la aplicación importamos todas las funciones que ejecutaremos al ingresar a las urls
from django.contrib.auth.views import LogoutView
from app.views import *


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

    #urls de las vistas basadas en clases
    path('lista-inquilino/', ListaIquilino.as_view(), name='lista_inquilinos'),
    path('detalle-inquilino/<pk>', InquilinoDetail.as_view(), name='detalle_inquilino'), # aquellas urls cuyas clases necesitan recuperar registros de la base de datos, necesitan el parámetro <pk> para identificar el registro con el que se quiere operar 
    path('crea-inquilino/', InquilinoCreate.as_view(), name='crear_inquilino'),
    path('actualiza-inquilino/<pk>', InquilinoUpdate.as_view(), name='actualizar_inquilino'),
    path('elimina-inquilino/<pk>', InquilinoDelete.as_view(), name='eliminar_inquilino'),
    

    #urls para el inicio de sesión
    path('login/', login_view, name='login'),
    path('registrar/', register, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    #url para editar perfil
    path('editar_perfil/', editar_perfil, name='editar_perfil'),

    #url para editar el avatar
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),



]
