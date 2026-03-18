#Creación de archivo urls.py
#Cuando se entre en la ruta vacía de esta app se ejecutara la vista inicio
#Agregamos ruta productos
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inicio, lista_productos, crear_producto, dashboard_view

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', lista_productos, name='productos'),
    path('productos/nuevo/', crear_producto, name='crear_producto'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]