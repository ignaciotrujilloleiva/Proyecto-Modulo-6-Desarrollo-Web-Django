# 🏢 Alke Web Base

<p align="center">
  <img src="https://img.shields.io/badge/Django-Web%20Framework-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Estado-Finalizado-success?style=for-the-badge" alt="Estado">
  <img src="https://img.shields.io/badge/Bootcamp-M%C3%B3dulo%206-orange?style=for-the-badge" alt="Bootcamp">
</p>

<p align="center">
  Aplicación web desarrollada con <strong>Django</strong> como parte del Módulo 6 del bootcamp, orientada a implementar una arquitectura web completa utilizando el patrón <strong>Modelo - Vista - Template (MVT)</strong>.
</p>

---

## 🚀 Descripción del proyecto

**Alke Web Base** es una aplicación web que permite:

* Visualizar productos almacenados en base de datos
* Registrar nuevos productos mediante formularios web
* Administrar información desde el panel administrativo de Django
* Gestionar acceso de usuarios mediante autenticación (login/logout)
* Restringir acceso a vistas protegidas

Este proyecto integra los principales componentes de Django en una solución funcional.

---

## 🧠 Tecnologías utilizadas

* Python 3
* Django
* HTML5
* CSS3
* SQLite3
* Visual Studio Code

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone 
https://github.com/ignaciotrujilloleiva/Proyecto-Modulo-6-Desarrollo-Web-Django.git
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Instalar dependencias

```bash
pip install django
```

---

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```
```bash
Credenciales utilizadas
Username: admin
Password: admin1234
```
---

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

---

### 8. Acceder al sistema

* 🌐 Aplicación: http://127.0.0.1:8000/
* ⚙️ Admin: http://127.0.0.1:8000/admin/
* 🔐 Login: http://127.0.0.1:8000/login/

---

## 🔐 Autenticación

El sistema implementa autenticación usando herramientas integradas de Django:

* Inicio de sesión mediante `LoginView` 
* Cierre de sesión mediante `LogoutView`
* Protección de vistas con `@login_required`
* Redirecciones configuradas desde `settings.py`

---

## 📌 Funcionalidades principales

* 📄 Página de inicio
* 📦 Listado de productos (dinámico)
* ➕ Registro de productos mediante formulario
* 🔐 Sistema de autenticación (login/logout)
* 🛂 Dashboard protegido
* ⚙️ Panel administrativo Django

---

## 🗃️ Modelo principal

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
```

---

## 🏗️ Arquitectura del proyecto

El proyecto sigue el patrón MVT (Modelo - Vista - Template) de Django:

```
Modelo → Vista → Template → Usuario
```

Esto permite separar:

* la lógica de datos
* la lógica de negocio
* la presentación visual

---

## 🧩 Estructura del proyecto

El código está modularizado para garantizar la escalabilidad:

```
/Proyecto-Modulo-6-Desarrollo-Web-Django
│
├── db.sqlite3
├── manage.py
├── README.md
│
├── Entregable/
│   └── Informe-proyecto-Alke-Web-Base.pdf
│
├── venv/
│
├── alke_web/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── webapp/
    ├── migrations/
    ├── static/
    │   └── webapp/
    │       └── style.css
    ├── templates/
    │   └── webapp/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── productos.html
    │       ├── crear_producto.html
    │       ├── login.html
    │       └── dashboard.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── test.py
    ├── urls.py
    └── views.py
```
---

## 🔍 Explicación de componentes importantes

`manage.py`

Archivo principal de administración del proyecto. Permite ejecutar comandos como:

* `runserver`
* `migrate`
* `makemigrations`
* `createsuperuser`

`settings.py`

Contiene la configuración global del proyecto:

* aplicaciones instaladas
* base de datos
* archivos estáticos
* templates
* autenticación

`urls.py`

Define las rutas del proyecto y conecta las rutas de la app principal mediante `include()`.

`models.py`

Define la estructura de la base de datos. En este proyecto, el modelo principal es `Producto`.

`views.py`

Contiene la lógica del sistema, como:

* renderizado de páginas
* consulta de productos
* procesamiento de formularios
* dashboard protegido

`forms.py`

Define formularios basados en modelos (`ModelForm`) para registrar productos desde la web.

`templates/`

Contiene las plantillas HTML del sistema:

* `base.html` → estructura reutilizable
* `inicio.html` → página principal
* `productos.html` → lista dinámica de productos
* `crear_producto.html` → formulario de creación
* `login.html` → autenticación
* `dashboard.html` → panel protegido

`static/`

Contiene los archivos estáticos del proyecto, como la hoja de estilos CSS.

`admin.py`

Registra modelos en el panel administrativo y permite personalizar su visualización.

`migrations/`

Gestiona los cambios en la base de datos mediante migraciones.

---

## 🧪 Pruebas realizadas

Durante el desarrollo se verificó:

* creación de productos desde el panel admin
* registro de productos mediante formulario web
* validación automática de formularios
* autenticación correcta e incorrecta
* acceso restringido a dashboard
* corrección del error 405 en logout, reemplazando GET por POST

---

## 📷 Evidencias

Se incluyen capturas de:

* Estructura del proyecto
* Funcionamiento del sistema
* Formularios
* Panel administrativo
* Autenticación

---

## 📌 Conclusión

Este proyecto permitió aplicar los conceptos fundamentales de Django, integrando base de datos, vistas dinámicas, formularios y autenticación en una aplicación web funcional, demostrando el flujo completo de desarrollo en el framework.

---

## ✍️ Autor
Ignacio Trujillo Leiva  
Bootcamp Fullstack Python  
2026
