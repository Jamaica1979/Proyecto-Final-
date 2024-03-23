from django.http import HttpResponse
from django.shortcuts import render
from AppFinance.models import *
from AppFinance.form import *

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Pagina de Inicio
def inicio(request):

    #imagen=request.user.avatar_set.first().imagen.url

    return render (request, "AppFinance/inicio.html")

#Descripcion sobre el autor
def aboutme (request):
    
    return render (request, "AppFinance/aboutme.html")

#Registro/login/logout
def iniciar_sesion(request):
    
    if request.method =='POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username') 
            contra = form.cleaned_data.get('password')   

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render (request, 'AppFinance/inicio.html', {'mensaje': f"Hola {user}"})
        
        else:
            return render (request,'AppFinance/inicio.html', {'mensaje': "Datos Incorrectos"})
    else:

        form = AuthenticationForm()

    return render (request, 'AppFinance/Registro/login.html', {'formulario': form})

    
def registrarse(request):
    if request.method == "POST":

        form = Registro_Usuario(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, "AppFinance/inicio.html",{"mensaje": 'Usuario creado correctamente'})
    
    else:

        form = Registro_Usuario()

    return render (request, "AppFinance/Registro/registro.html", {"formulario": form})
    
@login_required
def editar_usuario (request):
    
    usuario = request.user

    if request.method == "POST":

        form = Editar_Usuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info['email']
           #usuario.set_password(info['password']) - no va mas
            usuario.first_name = info ['first_name']
            usuario.last_name = info ['last_name']

            usuario.save()

            return render (request, "AppFinance/inicio.html")

    else:
        form = Editar_Usuario(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render (request, 'AppFinance/Registro/editar_usuario.html',{'formulario':form, 'usuario':usuario})

@login_required
def addAvatar (request):
    if request.method == "POST":

        formulario = form_Avatar(request.POST, request.FILES)

        if formulario.is_valid():

            info = formulario.cleaned_data
                                    
            usuario_actual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuario_actual, imagen=info["imagen"])

            avatar.save()

            return render(request, "AppFinance/inicio.html", {"mensaje":"Avatar Activado"})
    
    else:

        formulario = form_Avatar()

    return render(request, "AppFinance/Registro/nuevo_avatar.html", {"formulario": formulario})

class CambiarContra(LoginRequiredMixin, PasswordChangeView):

    template_name = "AppFinance/Registro/cambiar_contra.html"
    success_url = "/AppFinance/"

def cerrar_sesion(request):
    
    logout(request)
    return render (request, "AppFinance/Registro/cerrar_sesion.html", {'mensaje':"Sesión Finalizada"})

#CRUD de los MODELOS

#CRUD de Ingresos. Vistas Basadas en Clases
class ListaIngreso(LoginRequiredMixin, ListView):
    model = Ingreso

class DetalleIngreso(LoginRequiredMixin, DetailView):
    model = Ingreso

class CrearIngreso(LoginRequiredMixin, CreateView):
    model = Ingreso
    success_url = "/AppFinance/ingreso/list"
    fields = ['fecha' , 'importe', 'categoria', 'descripcion']

class ActualizarIngreso(LoginRequiredMixin, UpdateView):
    model = Ingreso
    success_url = "/AppFinance/ingreso/list"
    fields = ['fecha' , 'importe', 'categoria', 'descripcion']

class BorrarIngreso(LoginRequiredMixin, DeleteView):
    model = Ingreso
    success_url = "/AppFinance/ingreso/list"


#CRUD de Egresos. Vistas basadas en clases
class ListaEgreso(LoginRequiredMixin, ListView):
    model = Egreso

class DetalleEgreso(LoginRequiredMixin, DetailView):
    model = Egreso

class CrearEgreso(LoginRequiredMixin, CreateView):
    model = Egreso
    success_url = "/AppFinance/egreso/list"
    fields = ['fecha' , 'importe', 'categoria', 'descripcion']

class ActualizarEgreso(LoginRequiredMixin, UpdateView):
    model = Egreso
    success_url = "/AppFinance/egreso/list"
    fields = ['fecha' , 'importe', 'categoria', 'descripcion']

class BorrarEgreso(LoginRequiredMixin, DeleteView):
    model = Egreso
    success_url = "/AppFinance/egreso/list"


#CRUD de Cuentas. Vistas Basadas en Clases
class ListaCuenta(LoginRequiredMixin, ListView):
    model = Cuenta

class DetalleCuenta(LoginRequiredMixin, DetailView):
    model = Cuenta

class CrearCuenta(LoginRequiredMixin, CreateView):
    model = Cuenta
    success_url = "/AppFinance/cuenta/list"
    fields = ['tipo' , 'nombre']

class ActualizarCuenta(LoginRequiredMixin, UpdateView):
    model = Cuenta
    success_url = "/AppFinance/cuenta/list"
    fields = ['tipo' , 'nombre']

class BorrarCuenta(LoginRequiredMixin, DeleteView):
    model = Cuenta
    success_url = "/AppFinance/cuenta/list"


#CRUD de Reporte. Vistas Basadas en Clases
class Reporte():
    model=Ingreso
    model=Egreso
    fields = ['ingreso', 'egreso']
    def balance (self,inputs):
        inputs = ['ingreso', 'egreso']
        return Ingreso.importe - Egreso.importe

#Busqueda del models Ingreso
def buscar_ingreso(request):
    
    return render(request, "AppFinance/inicio.html")

def resultados_ingreso(request):

    if request.GET['descripcion']:
    
        descripcion = request.GET['descripcion']

        resultados = Ingreso.objects.filter(descripcion__icontains=descripcion)

        return render (request, "AppFinance/inicio.html",{'resultados':resultados})

    else:
        #respuesta = "No ingresaste datos"
    
        return render(request, "AppFinance/inicio.html")

    #return HttpResponse(respuesta)

    class probandogitignore():
        pass
