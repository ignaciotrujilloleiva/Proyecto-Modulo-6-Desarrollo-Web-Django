#Creación de archivo urls.py
#Cuando se entre en la ruta vacía de esta app se ejecutara la vista inicio
from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
]