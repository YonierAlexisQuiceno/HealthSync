# HealthSync
# 📅 Software de Gestión de Citas Médicas  
**Clínica Señora del Perpetuo Socorro**

## 📖 Descripción
Este proyecto consiste en el desarrollo de un sistema de **gestión de citas médicas**, diseñado para optimizar el agendamiento, modificación y cancelación de citas en la **Clínica Señora del Perpetuo Socorro**.  

El software busca reemplazar los procesos manuales de agendamiento (cuadernos, llamadas telefónicas) por una **plataforma digital centralizada**, mejorando la experiencia de los pacientes y facilitando el trabajo del personal administrativo y médico.

---

## ✨ Características principales
- 📌 **Gestión de citas**: agendar, modificar, cancelar y cerrar citas.  
- 📌 **Disponibilidad en tiempo real** de médicos y consultorios.  
- 📌 **Administración de pacientes y médicos** con base de datos relacional.  
- 📌 **Recordatorios automáticos** a pacientes (48h y 24h antes de la cita).  
- 📌 **Panel administrativo** con interfaz simple (≤ 3 pasos por acción).  
- 📌 **Seguridad e integridad de datos** mediante validaciones y restricciones.  

---

## 🛠️ Tecnologías utilizadas
- **Lenguaje backend**: *(Python )*  
- **Base de datos**: PostgreSQL  
- **Frontend**: *()*  
- **ORM / Framework**: *(Python y flask)*  

---

## ⚙️ Instalación y configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/YonierAlexisQuiceno/HealthSync.git
   cd HealthSync
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la base de datos PostgreSQL:
   ```sql
   
   ```

4. Ejecutar migraciones de tablas (pacientes, médicos, especialidades, consultorios, citas):
   ```bash

   ```

5. Iniciar el servidor:
   ```bash

   ```

---

## 🚀 Uso
- **Administrador**:  
  - Crear, editar o cancelar citas.  
  - Ver disponibilidad de médicos y consultorios.  
  - Gestionar pacientes, médicos y especialidades.  

- **Paciente**:  
  - Recibir notificaciones automáticas.  
  - Confirmar o cancelar citas mediante enlace.  

---

## 📊 Modelo de datos
El sistema se basa en una base de datos **relacional normalizada** en PostgreSQL con las siguientes tablas:
- **Pacientes**
- **Médicos**
- **Especialidades**
- **Consultorios**
- **Citas**

---

## 👨‍💻 Autores
- Yonier Alexis Quiceno Rodríguez  
- Andrés Jaramillo López  
- Eulices Morales  

**Institución Universitaria Digital de Antioquia**  
Semestre 3 – 2025  

---

## Licencia
Este proyecto se distribuye bajo la licencia **MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito a los autores.
