from django.urls import path
from .views import *


urlpatterns = [
    path('', home,name="home"),
    path('login', login,name="login"),
    path('articulos', articulos,name="articulos"),
    path('limpiar', limpiar),
    path('carrito', carrito,name="carrito"),
    path('historial', historial,name="historial" ),
    path('seguimiento', seguimiento,name="seguimiento" ),
    path('crudProductos', crudProductos,name="crudProductos" ),
    path('registro', registro ,name="registro" ),
    path('suscripcion', suscripcion,name="suscripcion" ),
    path('agregar', agregar, name="agregar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('agregar_al_carro/<str:id>', agregar_al_carro, name="agregar_al_carro"),
    path('elimnar_del_carro/<str:id>', eliminar_del_carro, name="eliminar_del_carro"),
    path('comprar/', comprar, name="comprar"),
    path('suscribir/', suscribir, name="suscribir"),
]
