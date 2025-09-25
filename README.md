🏥 HealthSync — Gestión de Citas Médicas

Clínica Señora del Perpetuo Socorro
Proyecto académico — Institución Universitaria Digital de Antioquia (Semestre 3, 2025)

📖 Descripción

HealthSync es un sistema de gestión de citas médicas que optimiza el agendamiento, modificación y cancelación de citas en la Clínica Señora del Perpetuo Socorro.

Busca reemplazar procesos manuales (cuadernos, llamadas) con una plataforma digital centralizada, mejorando la experiencia de pacientes y facilitando la labor administrativa y médica.

✨ Características principales

📌 Gestión de citas: agendar, modificar, cancelar y cerrar.

📌 Disponibilidad en tiempo real de médicos y consultorios.

📌 Administración de pacientes y médicos con base de datos relacional.

📌 Recordatorios automáticos (48h y 24h antes de la cita).

📌 Panel administrativo simple (≤ 3 pasos por acción).

📌 Seguridad e integridad de datos mediante validaciones.

🛠️ Tecnologías utilizadas

Backend: Python 3.9+, Django 4.2

Base de datos: PostgreSQL 12+ (probado en 17)

ORM: Django ORM

Frontend: HTML/CSS/JS + templates de Django

📂 Estructura del proyecto
HealthSync/
├─ venv/                          # entorno virtual (no se versiona)
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

⚙️ Instalación y configuración
1. Clonar repositorio
git clone https://github.com/YonierAlexisQuiceno/HealthSync.git
cd HealthSync/UNIVERSITYPROJECT


El entorno virtual venv se ubica un nivel arriba de la carpeta con manage.py.

2. Crear y activar entorno virtual
Windows (PowerShell)
python -m venv ..\venv
..\venv\Scripts\activate


Si PowerShell bloquea scripts:
..\venv\Scripts\activate.bat o
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass.

macOS / Linux
python3 -m venv ../venv
source ../venv/bin/activate

3. Instalar dependencias

Si el repo trae requirements.txt:

pip install -r requirements.txt


Mínimo necesario:

pip install "Django==4.2.*" "psycopg[binary]" tzdata
# Alternativa: pip install psycopg2-binary

4. Configurar PostgreSQL
CREATE DATABASE citas_medicas;
ALTER USER postgres WITH PASSWORD 'tu_password_seguro';


En UNIVERSITYPROJECT/settings.py:

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

5. Migraciones, superusuario y servidor
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


App: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

🚀 Uso
Roles

Administrador: gestiona citas, pacientes, médicos, consultorios y especialidades.

Paciente: recibe notificaciones y confirma/cancela citas.

Rutas de ejemplo

/ — Home

/pacientes/

/medicos/

/citas/

/citas/agregar/

/citas/hoy/

/admin/

📊 Modelo de datos

Tablas principales:

Pacientes

Médicos

Especialidades

Consultorios

Citas

🛠️ Problemas comunes y soluciones

Error loading psycopg2 or psycopg module → pip install "psycopg[binary]".

getaddrinfo failed → cambia HOST a 127.0.0.1.

password authentication failed → revisa credenciales en PostgreSQL y settings.py.

psql: command not found en Windows → agrega PostgreSQL a PATH o usa pgAdmin.

PowerShell no activa venv → usar .bat o Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass.

Python apunta al sistema en Windows → desactivar App execution aliases o alias temporal:
Set-Alias python "..\venv\Scripts\python.exe".

👨‍💻 Autores

Yonier Alexis Quiceno Rodríguez

Andrés Jaramillo López

Eulices Morales

Institución Universitaria Digital de Antioquia
Semestre 3 — 2025

📜 Licencia

Este proyecto se distribuye bajo licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito a los autores.
