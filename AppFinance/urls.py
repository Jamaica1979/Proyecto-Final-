from django.urls import path
from AppFinance.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [

    #url de Inicio
    path('', inicio, name= 'Inicio'),
    #url del About
    path("about/", aboutme, name='Acerca de Mi'),
    #url de registro
    path("login/", iniciar_sesion, name = "Login"),
    path("register/", registrarse, name = "Registro"),
    #path("logout", LogoutView.as_view(template_name="AppFinance/cerrar_sesion.html"), name='Logout'),
    #no me funciono el "cerrar sesion" con clases.
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
    path("editar/", editar_usuario, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contraseña"),
    #url de avatar
    path("avatar/", addAvatar, name="Agregar Avatar"),



    #url de los CRUD basadas en Clases
    
    #CRUD del model "ingreso"
   
    path('ingreso/list', ListaIngreso.as_view(), name = 'IngresosLeer'),
    path('ingreso/<int:pk>', DetalleIngreso.as_view(), name = 'IngresosDetalle'),
    path('ingreso/crear/', CrearIngreso.as_view(), name = 'IngresosCrear'),
    path('ingreso/editar/<int:pk>', ActualizarIngreso.as_view(), name = 'IngresosEditar'),
    path('ingreso/borrar/<int:pk>', BorrarIngreso.as_view(), name = 'IngresosEliminar'),

    #Crud de Cuentas
    path('cuenta/list', ListaCuenta.as_view(), name = 'CuentasLeer'),
    path('cuenta/<int:pk>', DetalleCuenta.as_view(), name = 'CuentasDetalle'),
    path('cuenta/crear/', CrearCuenta.as_view(), name = 'CuentasCrear'),
    path('cuenta/editar/<int:pk>', ActualizarCuenta.as_view(), name = 'CuentasEditar'),
    path('cuenta/borrar/<int:pk>', BorrarCuenta.as_view(), name = 'CuentasEliminar'),

    #CRUD de egreso
    path('egreso/list', ListaEgreso.as_view(), name = 'EgresosLeer'),
    path('egreso/<int:pk>', DetalleEgreso.as_view(), name = 'EgresosDetalle'),
    path('egreso/crear/', CrearEgreso.as_view(), name = 'EgresosCrear'),
    path('egreso/editar/<int:pk>', ActualizarEgreso.as_view(), name = 'EgresosEditar'),
    path('egreso/borrar/<int:pk>', BorrarEgreso.as_view(), name = 'EgresosEliminar'),

    #url de busqueda
    path('buscar/', buscar_ingreso, name='Buscar'),
    path('resultados/', resultados_ingreso, name='Resultados'),




]
