#Ahora se utilizara render
from django.shortcuts import render
#Se importa HttpResponse
from django.http import HttpResponse

# Create your views here.

#Creación de vista

#Django renderiza un archivo HTML

def inicio(request):
    return render(request, 'webapp/inicio.html')