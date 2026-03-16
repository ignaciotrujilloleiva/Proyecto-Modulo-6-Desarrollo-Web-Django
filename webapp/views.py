from django.shortcuts import render
#Se importa HttpResponse
from django.http import HttpResponse

# Create your views here.

#Creación de vista
#Request recibe solicitud del navegador
#HttpResponse devuelve una respuesta que seria el texto de bienvenida

def inicio(request):
    return HttpResponse("Bienvenido a Alke Web Base")