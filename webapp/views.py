#Ahora se utilizara render
from django.shortcuts import render, redirect
#Importación de modelo producto
from .models import Producto
from .forms import ProductoForm

# Create your views here.

#Creación de vista

#Django renderiza un archivo HTML

def inicio(request):
    return render(request, 'webapp/inicio.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'webapp/productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()

    return render(request, 'webapp/crear_producto.html', {'form': form})