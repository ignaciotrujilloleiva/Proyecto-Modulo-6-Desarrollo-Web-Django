#Ahora se utilizara render
from django.shortcuts import render
#Se importa HttpResponse
from django.http import HttpResponse
#Importación de modelo producto
from .models import Producto

# Create your views here.

#Creación de vista

#Django renderiza un archivo HTML

def inicio(request):
    return render(request, 'webapp/inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'webapp/productos.html', {'productos': productos})