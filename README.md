# HealthSync — Gestión de Citas Médicas

Clínica Señora del Perpetuo Socorro
Proyecto académico — Institución Universitaria Digital de Antioquia (Semestre 3, 2025)

## Descripción

HealthSync es un sistema de gestión de citas médicas que optimiza el agendamiento, modificación y cancelación de citas en la Clínica Señora del Perpetuo Socorro.

Busca reemplazar procesos manuales (cuadernos, llamadas) con una plataforma digital centralizada, mejorando la experiencia de pacientes y facilitando la labor administrativa y médica.

✨ Características principales

📌 Gestión de citas: agendar, modificar, cancelar y cerrar.

📌 Disponibilidad en tiempo real de médicos y consultorios.

📌 Administración de pacientes y médicos con base de datos relacional.

📌 Panel administrativo simple (≤ 3 pasos por acción).

📌 Seguridad e integridad de datos mediante validaciones.

## Tecnologías utilizadas

Backend: Python 3.9+, Django 4.2

Base de datos: PostgreSQL 12+ (probado en 17)

ORM: Django ORM

Frontend: HTML/CSS/JS + templates de Django

## Estructura del proyecto

```text
HealthSync/
├─ venv/             # entorno virtual (no se versiona)
└─ UNIVERSITYPROJECT/
   ├─ manage.py
   ├─ UNIVERSITYPROJECT/
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py / asgi.py
   └─ clinica/
      ├─ migrations/
      ├─ templates/
      ├─ static/
      ├─ models.py
      ├─ views.py
      ├─ urls.py
      └─ admin.py
```
### Instalación y configuración
1. Clonar repositorio
```bash 
git clone https://github.com/YonierAlexisQuiceno/HealthSync.git
cd HealthSync/UNIVERSITYPROJECT
```

2. Configurar PostgreSQL
CREATE DATABASE citas_medicas;
ALTER USER postgres WITH PASSWORD 'tu_password_seguro';


En UNIVERSITYPROJECT/settings.py:

organiza este arcvhivo segun sus credenciales de posgres

organiza este archivo segun sus credenciales de postgres

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'citas_medicas',
        'USER': 'postgres',
        'PASSWORD': 'tu_password_seguro',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
TIME_ZONE = 'America/Bogota'
```
### Creación y Activación del Entorno Virtual (.venv)

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1     
pip install --upgrade pip
```
### Instalación de Django y Django REST Framework

```bash
pip install django
pip install djangorestframework
```
### Navegar al Directorio Principal del Proyecto (UNIVERSITYPROJECT)

```bash
cd .\UNIVERSITYPROJECT\
```
### Instalar el Controlador de Base de Datos para PostgreSQL

```bash
python.exe -m pip install psycopg2-binary
```
### Aplicar Migraciones a la Base de Datos

```bash
python manage.py makemigrations
python manage.py migrate
```
### Crear el Superusuario Administrador

```bash
python manage.py createsuperuser
```
### Iniciar el Servidor de Desarrollo
 
```bash
python manage.py runserver 
```


App: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

## Uso Roles

Administrador: gestiona citas, pacientes, médicos, consultorios y especialidades.

Paciente: recibe notificaciones y confirma/cancela citas.

Rutas de ejemplo



## Modelo de datos

Tablas principales:

Pacientes

Médicos

Especialidades

Consultorios

Citas



## Autores

Yonier Alexis Quiceno Rodríguez

Andrés Jaramillo López

Eulices Morales

Institución Universitaria Digital de Antioquia
Semestre 3 — 2025

## Licencia

Este proyecto se distribuye bajo licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito a los autores.
