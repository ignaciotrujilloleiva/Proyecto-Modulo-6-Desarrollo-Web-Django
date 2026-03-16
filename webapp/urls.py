#Creación de archivo urls.py
#Cuando se entre en la ruta vacía de esta app se ejecutara la vista inicio
#Agregamos ruta productos
from django.urls import path
from .views import inicio, lista_productos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', lista_productos, name='productos'),
]