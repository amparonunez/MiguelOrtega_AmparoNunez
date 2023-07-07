from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests

def home(request):
    return render(request, 'core/index.html')


def articulos(request):
    plantas = Producto.objects.all()
    return render(request, 'core/articulos.html', {'plantas':plantas, 'carro': request.session.get("carro", [])})

def carrito(request):
    context = {"carro":request.session.get("carro",[])}
    suscrito(request, context)
    print(context)
    return render(request, 'core/carrito.html', context)

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] =  resp.json()["mensaje"]
            suscrito(request, context)
            return render(request, 'core/suscripcion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    
def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

@login_required(login_url="login")
def historial(request):
    detalles = DetalleVenta.objects.all()
    context = {
        'detalles': detalles
    }
    return render(request, 'core/historial.html', context)

def seguimiento(request):
    return render(request, 'core/seguimiento.html')

@login_required(login_url="login")
def crudProductos(request):
    productos = Producto.objects.all().order_by('codigo')
    datos = {
        'productos' : productos
    }
    return render(request, 'core/crudProductos.html', datos)

@login_required(login_url="login")
def agregar(request):
    datos = {
        'form': productosForm
    }
    if request.method=='POST':
        productos_form = productosForm(data=request.POST, files=request.FILES)
        if productos_form.is_valid():
            productos_form.save()
            return redirect(to="lista_productos")
        else:
            datos['form'] = productos_form
    
    return render(request, 'core/agregar.html', datos)

@login_required(login_url="login")
def modificar(request, id):
    productos = get_object_or_404(Producto, codigo=id)
    datos = {
        'form': productosForm(instance = productos)
    }
    if request.method=='POST':
        formulario = productosForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="crudProductos")
        datos["form"] = formulario
              
    return render(request, 'core/modificar.html', datos)

@login_required(login_url="login")
def eliminar(request, id):
    productos = get_object_or_404(Producto, codigo=id)
    productos.delete()
    return redirect(to="crudProductos") 


def registro(request):
    datos = {
        'form': registroForm()
    }

    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        else:
            datos['form'] = formulario
    
    return render (request, 'registration/registro.html', datos)

def suscripcion(request):
    return render(request, 'core/suscripcion.html')

#Carrito de compras
def agregar_al_carro(request, id):
    producto = Producto.objects.get(codigo=id)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([id, producto.detalle, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="articulos")

def eliminar_del_carro(request, id):
    carro = request.session.get("carro", [])
    for item in carro:
            
        if item[0] == id:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="articulos")

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.stock = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []

    return redirect(to="carrito")


