from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
import requests

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
    messages.success(request, "Compra realizada!.")
    for item in carro:
        detalle = Detalleventa()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        
        detalle.producto.stock -= detalle.cantidad
        detalle.producto.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def carrito(request):
    return render(request, 'core/carrito.html', {"carro":request.session.get("carro", [])})


def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def addtocar(request, codigo):
    productodestacado = Producto.objects.get(codigo = codigo)         
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4]+= 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([codigo, productodestacado.detalle, productodestacado.imagen, productodestacado.precio, 1, productodestacado.precio])
    request.session["carro"] = carro
    return redirect(to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="home") 

def home(request):
    plantas = Producto.objects.filter(destacado=True)

    return render(request, 'core/index.html', {'planta':plantas, "carro":request.session.get("carro", [])})

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    else:
        return render(request, 'core/suscripcion.html', context)

def semillas(request):
    semillas = Producto.objects.filter(categoria="semilla")
    return render(request, 'core/semillas.html', {'semilla':semillas, "carro":request.session.get("carro", [])})

def herramientas(request):
    herramientas = Producto.objects.filter(categoria="herramienta")
    return render(request, 'core/herramientas.html', {'herramienta':herramientas, "carro":request.session.get("carro", [])})

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            messages.success(request, "Registrado correctamente!.")
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form':registro})

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {"compras":compras})

def detalle(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    detalles = Detalleventa.objects.filter(cliente=request.user)
    return render(request, 'core/detalle.html', {"detalles":detalles})