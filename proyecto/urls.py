
from django.contrib import admin
from django.urls import path, include
#importaciones necesarias para trabajar con imágenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # rediccionamos las busquedas de las urls al archivo urls.py creado en la carpeta de la aplicación. 
    path('', include('app.urls'))     
]

#configuración necesaria que me permite buscar las imágenes que usaremos en la aplicación
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
