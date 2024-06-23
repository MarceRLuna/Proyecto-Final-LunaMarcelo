
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # rediccionamos las busquedas de las urls al archivo urls.py creado en la carpeta de la aplicación. 
    path('', include('app.urls')) 
]
