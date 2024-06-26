
from django.http import HttpResponse 
from django.shortcuts import render
from .models import Inmueble, Propietario, Inquilino, Avatar  # importamos los modelos que utilizaremos en las funciones
from .forms import Inmueble_Formulario, Inquilino_Formulario, Propietario_Formulario, UserEditForm, Avatar_Formulario
from django.views.generic import ListView # nos permite construir la vista en listado de nuestros ítems en nuestro modelo
from django.views.generic.detail import DetailView # nos permite construir la vista en detalle de un determinado ítem de nuestro modelo
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required


# --------------------- Vistas basadas en funciones -------------------------------.

def inicio(req):
    try:
        avatar = Avatar.objects.get(user = req.user.id)
        return render(req, "inicio.html", {'url': avatar.imagen.url})
    except:
         return render(req, "inicio.html", {})  


@staff_member_required(login_url='/login/')
def inmueble_formulario(req):

    if req.method == 'POST':

        avatar = Avatar.objects.get(user = req.user.id)

        mi_formulario_inmueble = Inmueble_Formulario(req.POST)

        if mi_formulario_inmueble.is_valid():

            data = mi_formulario_inmueble.cleaned_data

            # creamos una instancia de la clase Inmueble.
            nuevo_inmueble = Inmueble(categoria=data['categoria'], ubicacion=data['ubicacion'], domitorios=data['domitorios'], metros_cuadrados=data['metros_cuadrados']) 
    
            nuevo_inmueble.save() # con el método .save() guardamos en la base de datos la instancia que creamos.

            return render(req, "message.html", {"message": "Inmueble creado con éxito", 'url': avatar.imagen.url})
        
        else:
            return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})
    else:
        mi_formulario_inmueble = Inmueble_Formulario()

        avatar = Avatar.objects.get(user = req.user.id)

        return render(req, "inmueble_formulario.html", {"mi_formulario_inmueble": mi_formulario_inmueble, 'url': avatar.imagen.url})
    


@login_required()
def inquilino_formulario(req):
    
    # si se invoca a la función inquilino_formulario con una solicitud de tipo POST, significa que se clickeo el botón para enviar la información cargada al formulario y se ejecuta el código del if

    if req.method == 'POST':

        avatar = Avatar.objects.get(user = req.user.id)
        
        mi_formulario_inquilino = Inquilino_Formulario(req.POST) # almaceno en una variable todos los datos que se cargan en el formulario

        if mi_formulario_inquilino.is_valid(): # Utilizamos el método is_valid que tienen todos los formularios creados con la clase de Django From para validar los datos ingresados al formulario

            data = mi_formulario_inquilino.cleaned_data # Recuperamos los datos ya validados del formulario y los guardamos en la variable "data"

            # utilizamos la variable "data" para crear una instancia de la clase Inquilino
            nuevo_inquilino = Inquilino(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], mail=data['mail'], valor_alquiler=data['valor_alquiler'])

            nuevo_inquilino.save() # guardamos dicha instancia en nuestra base de datos con el método .save()

            return render(req, "message.html", {"message": "Datos del inquilino cargados con éxito", 'url': avatar.imagen.url}) # renderizamos el html "message" e imprimimos el mensaje almacenado en el contexto
        
        else:
            return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})
    
    else:
        # se ejecuta el siguiente código cuando se invoca a la función inquilino_formulario al ingresar a la url, es decir con la solicitud de tipo GET
        avatar = Avatar.objects.get(user = req.user.id)

        mi_formulario_inquilino = Inquilino_Formulario()

        return render(req, "inquilino_formulario.html", {"mi_formulario_inquilino": mi_formulario_inquilino, 'url': avatar.imagen.url})
    


@staff_member_required(login_url='/login/')
def propietario_formulario(req):

    
    if req.method == 'POST':

        avatar = Avatar.objects.get(user = req.user.id)

        mi_formulario_propietario = Propietario_Formulario(req.POST)

        if mi_formulario_propietario.is_valid():

            data = mi_formulario_propietario.cleaned_data
        
            nuevo_propietario = Propietario(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], mail=data['mail'])

            nuevo_propietario.save() 

            return render(req, "message.html", {"message": "Datos del propietario cargados con éxito", 'url': avatar.imagen.url})
        
        else:
            return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})
    
    else:
        avatar = Avatar.objects.get(user = req.user.id)

        mi_formulario_propietario = Propietario_Formulario()

        return render(req, "propietario_formulario.html", {"mi_formulario_propietario": mi_formulario_propietario, 'url': avatar.imagen.url})



def busqueda_inmueble(req): # esta función solo renderiza un html que se llama "busqueda_inmueble.html"
    
    try:
        avatar = Avatar.objects.get(user = req.user.id)
        return render(req, "busqueda_inmueble.html", {'url': avatar.imagen.url})
    except:
         return render(req, "busqueda_inmueble.html", {}) 



def buscar(req):

    try:
        avatar = Avatar.objects.get(user = req.user.id) 

        if req.GET["domitorios"]:

            domitorios = req.GET["domitorios"]

            inmueble = Inmueble.objects.filter(domitorios = domitorios) #guardamos en la variable "inmueble" al inmueble que coincida con el criterio de busqueda definido entre los paréntesis (), es decir, recupera el inmueble cuya cantidad de dormitorios sea igual a la cantidad de dormitorios que ingresa el usuario

            return render(req, "resultado_busqueda.html", {"inmueble": inmueble, "domitorios": domitorios, 'url': avatar.imagen.url})

        else:
             return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})       
    except:
         if req.GET["domitorios"]:

            domitorios = req.GET["domitorios"]

            inmueble = Inmueble.objects.filter(domitorios = domitorios) 

            return render(req, "resultado_busqueda.html", {"inmueble": inmueble, "domitorios": domitorios})

         else:
            return render(req, "message.html", {"message": "Datos inválidos"}) 

    

# función que permite leer y renderizar todos los registros guardados en la tabla "Inmueble" de la base de datos
def lista_inmuebles(req):

    try:
        avatar = Avatar.objects.get(user = req.user.id)

        mis_inmuebles = Inmueble.objects.all() # manager que me permite recuperar todos los datos almacenados en la tabla Inmueble, creada en la base de datos. En la variable "mis_inmuebles" guardamos la info.
        
        return render(req, "lista_inmuebles.html", {'url': avatar.imagen.url, "lista_inmuebles" : mis_inmuebles})
    except:
        mis_inmuebles = Inmueble.objects.all()
        return render(req, "lista_inmuebles.html", {"lista_inmuebles" : mis_inmuebles}) 


# función que permite eliminar un registro de la tabla "Inmueble"
@staff_member_required(login_url='/login/') # decorador que permite ingresar a la view solo si hay un usuario logueado y además tiene permiso de superUsuario
def eliminar_inmueble(req, id):

    inmueble_a_eliminar = Inmueble.objects.get(id=id) # recuperamos de la tabla el registro a eliminar que coincide con el criterio de busqueda del manager get(id=id)

    inmueble_a_eliminar.delete() # eliminamos el dato con el método .delete()

    mis_inmuebles = Inmueble.objects.all() # recuperamos todos los registros que quedan en la tabla "Inmueble"
                    
    return render(req, "lista_inmuebles.html", {"lista_inmuebles" : mis_inmuebles}) # renderizamos todos los registros 

                    
@login_required() # decorador que permite ingresar a la view solo si hay un usuario logueado.
# función que permite editar un registro de la tabla "Inmueble"
def editar_inmueble(req, id):

    if req.method == 'POST':
                
        mi_formulario_inmueble = Inmueble_Formulario(req.POST)

        if mi_formulario_inmueble.is_valid():

            # guardamos la inforación cargada por el usuario en los campos del formulario en la variable "data"
            data = mi_formulario_inmueble.cleaned_data

            # recuperamos la instancia que ya existe en la base de datos
            mi_inmueble = Inmueble.objects.get(id = id)

            # actualizamos los campos de dicha instancia con los datos cargados por el usuario, los cuales están guardados en la variable "data"
            mi_inmueble.categoria = data['categoria']
            mi_inmueble.ubicacion = data['ubicacion']
            mi_inmueble.domitorios = data['domitorios']
            mi_inmueble.metros_cuadrados = data['metros_cuadrados']

            # guardamos los datos actualizados en la tabla "Inmueble"
            mi_inmueble.save()

            return render(req, "message.html", {"message": "Inmueble actualizado con éxito"})
        
        else:
            return render(req, "message.html", {"message": "Datos inválidos"})
    else:

        mi_inmueble = Inmueble.objects.get(id = id) # en la variable "mi_inmueble" guardo los datos que contiene el registro cargado en la base de datos cuyo id coincida con el criterio de busqueda el manager .get(id = id)

        # a través del parámetro por nombre "initial={}" podemos definir los valores que queremos que tenga cada uo de los atributos definidos en el formulario al momento de renderizarse.
        mi_formulario_inmueble = Inmueble_Formulario(initial={
            "categoria": mi_inmueble.categoria,
            "ubicacion": mi_inmueble.ubicacion,
            "domitorios": mi_inmueble.domitorios,
            "metros_cuadrados": mi_inmueble.metros_cuadrados
        }) 

        return render(req, "editar_inmuebles.html", {"mi_formulario_inmueble": mi_formulario_inmueble, "id": mi_inmueble.id})



# -------------------- Vistas basadas en clases -------------------------------


class ListaIquilino (LoginRequiredMixin, ListView):

    model = Inquilino # utilizamos el modelo para buscar los registros de la tabla correspondiente
    template_name = 'inquilino_list.html' # definimos el html al que le pasaremos los registros como contexto
    context_object_name = 'inquilinos' # definimos el nombre de la variable de contexto
    
   

class InquilinoDetail (LoginRequiredMixin, DetailView):

    model = Inquilino
    template_name = 'inquilino_detail.html'
    context_object_name = 'inquilino'

class InquilinoCreate (LoginRequiredMixin, CreateView):

    model = Inquilino
    template_name = 'inquilino_create.html'
    fields = ['nombre', 'apellido', 'telefono', 'mail','valor_alquiler'] # atributo que recibe una lista y nos permite definir los campos que queremos que se visualizen a la hora de renderizar el formulario
    success_url = '/lista-inquilino/'

class InquilinoUpdate (LoginRequiredMixin, UpdateView):

    model = Inquilino
    template_name = 'inquilino_update.html'
    fields = ('__all__') # declarado de esta manera indicamos que se visualizan todos los campos.
    success_url = '/lista-inquilino/'
    context_object_name = 'inquilino'

class InquilinoDelete (LoginRequiredMixin, DeleteView):

    model = Inquilino
    template_name = 'inquilino_delete.html'
    success_url = '/lista-inquilino/'
    context_object_name = 'inquilino'    


 # ------------------------- Creación del login  ------------------------------------

def login_view(req):

    try:
        if req.method == 'POST':

            avatar = Avatar.objects.get(user = req.user.id)

            mi_formulario = AuthenticationForm(req, data=req.POST)

            if mi_formulario.is_valid():

                data = mi_formulario.cleaned_data
        
                usuario = data['username']
                psw = data['password']

                user = authenticate(username=usuario, password=psw)
            
                if user:
                    login(req, user)
                    return render(req, "message.html", {"message": f"Bienvenido {usuario}", 'url': avatar.imagen.url})
                else:
                    return render(req, "message.html", {"message": "Datos erróneos", 'url': avatar.imagen.url})
        
            else:
                return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})
    
        else:
            avatar = Avatar.objects.get(user = req.user.id)

            mi_formulario = AuthenticationForm()

            return render(req, "login.html", {"mi_formulario": mi_formulario, 'url': avatar.imagen.url})
    except:
         
        if req.method == 'POST':

            mi_formulario = AuthenticationForm(req, data=req.POST)

            if mi_formulario.is_valid():

                data = mi_formulario.cleaned_data
        
                usuario = data['username']
                psw = data['password']

                user = authenticate(username=usuario, password=psw)
            
                if user:
                    login(req, user)
                    return render(req, "message.html", {"message": f"Bienvenido {usuario}"})
                else:
                    return render(req, "message.html", {"message": "Datos erróneos"})
        
            else:
                return render(req, "message.html", {"message": "Datos inválidos"})
    
        else:
            
            mi_formulario = AuthenticationForm()

            return render(req, "login.html", {"mi_formulario": mi_formulario}) 

    
    

# ----------------------- Creación del registro de usuario ----------------------------

def register(req):

    try:
        if req.method == 'POST':

            avatar = Avatar.objects.get(user = req.user.id)

            mi_formulario = UserCreationForm(req.POST)

            if mi_formulario.is_valid():

                data = mi_formulario.cleaned_data
        
                usuario = data['username']
            
                mi_formulario.save()

                return render(req, "message.html", {"message": f"Usuario {usuario} creado con éxito", 'url': avatar.imagen.url})
        
            else:
                return render(req, "message.html", {"message": "Datos inválidos", 'url': avatar.imagen.url})
    
        else:
            avatar = Avatar.objects.get(user = req.user.id)
        
            mi_formulario = UserCreationForm()

            return render(req, "registro.html", {"mi_formulario": mi_formulario, 'url': avatar.imagen.url})
    except:
         
        if req.method == 'POST':

            mi_formulario = UserCreationForm(req.POST)

            if mi_formulario.is_valid():

                data = mi_formulario.cleaned_data
        
                usuario = data['username']
            
                mi_formulario.save()

                return render(req, "message.html", {"message": f"Usuario {usuario} creado con éxito"})
        
            else:
                return render(req, "message.html", {"message": "Datos inválidos"})
    
        else:
                    
            mi_formulario = UserCreationForm()

            return render(req, "registro.html", {"mi_formulario": mi_formulario})  

    
    

# ----------------------- Edición de perfil -------------------------------

@login_required()
def editar_perfil(req):

    

    usuario = req.user # recuperamos al usuario que envía la request
    
    avatar = Avatar.objects.get(user = req.user.id)

    if req.method == 'POST':
        
        mi_formulario_perfil = UserEditForm(req.POST, instance=req.user)

        if mi_formulario_perfil.is_valid():

            data = mi_formulario_perfil.cleaned_data
                      
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password_1'])            

            usuario.save()

            return render(req, "message.html", {"message": "Datos actualizado con éxito"})
        
        else:
            #return render(req, "message.html", {"message": "Datos inválidos"})
            return render(req, "editar_perfil.html", {"mi_formulario_perfil": mi_formulario_perfil, 'url': avatar.imagen.url})
    else:
      
       mi_formulario_perfil = UserEditForm(instance= req.user) 

       return render(req, "editar_perfil.html", {"mi_formulario_perfil": mi_formulario_perfil, 'url': avatar.imagen.url})
    
    

def agregar_avatar(req):
    
    if req.method == 'POST':
        
        mi_formulario_avatar = Avatar_Formulario(req.POST, req.FILES)

        if mi_formulario_avatar.is_valid():

            data = mi_formulario_avatar.cleaned_data
                      
            avatar = Avatar(user=req.user, imagen=data['imagen'])          

            avatar.save()

            return render(req, "message.html", {"message": "Avatar cargado con éxito"})
        
        else:
            return render(req, "message.html", {"message": "Datos inválidos"})
            
    else:
      
       mi_formulario_avatar = Avatar_Formulario() 

       return render(req, "agregar_avatar.html", {"mi_formulario_avatar": mi_formulario_avatar})
    

