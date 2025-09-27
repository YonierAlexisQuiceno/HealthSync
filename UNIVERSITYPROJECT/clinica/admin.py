from django.contrib import admin
from .models import Pacientes, Medicos, Especialidades, Consultorios, Citas

@admin.register(Especialidades)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['id_especialidad', 'nombre_especialidad']
    search_fields = ['nombre_especialidad']

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ['id_paciente', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_nacimiento']
    search_fields = ['nombre', 'apellido', 'correo']
    list_filter = ['fecha_nacimiento']
    ordering = ['apellido', 'nombre']

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ['id_medico', 'nombre', 'apellido', 'cedula_profesional', 'get_especialidad']
    search_fields = ['nombre', 'apellido', 'cedula_profesional']
    list_filter = ['id_especialidad']
    ordering = ['apellido', 'nombre']
    
    def get_especialidad(self, obj):
        return obj.id_especialidad.nombre_especialidad
    get_especialidad.short_description = 'Especialidad'

@admin.register(Consultorios)
class ConsultoriosAdmin(admin.ModelAdmin):
    list_display = ['id_consultorio', 'numero_consultorio']
    search_fields = ['numero_consultorio']

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = ['id_cita', 'get_paciente', 'get_medico', 'fecha_cita', 'hora_cita', 'estado', 'get_consultorio']
    list_filter = ['fecha_cita', 'estado', 'id_medico__id_especialidad']
    search_fields = ['id_paciente__nombre', 'id_paciente__apellido', 'id_medico__nombre', 'id_medico__apellido']
    date_hierarchy = 'fecha_cita'
    ordering = ['-fecha_cita', '-hora_cita']
    
    def get_paciente(self, obj):
        return f"{obj.id_paciente.nombre} {obj.id_paciente.apellido}"
    get_paciente.short_description = 'Paciente'
    
    def get_medico(self, obj):
        return f"Dr. {obj.id_medico.nombre} {obj.id_medico.apellido}"
    get_medico.short_description = 'Médico'
    
    def get_consultorio(self, obj):
        return obj.id_consultorio.numero_consultorio
    get_consultorio.short_description = 'Consultorio'