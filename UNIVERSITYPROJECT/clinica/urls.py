from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Pacientes
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/agregar/', views.agregar_paciente, name='agregar_paciente'),
    path('pacientes/<int:paciente_id>/', views.detalle_paciente, name='detalle_paciente'),
    
    # Médicos
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('medicos/agregar/', views.agregar_medico, name='agregar_medico'),
    path('medicos/<int:medico_id>/', views.detalle_medico, name='detalle_medico'),
    
    # Citas
    path('citas/', views.listar_citas, name='listar_citas'),
    path('citas/agregar/', views.agregar_cita, name='agregar_cita'),
    path('citas/<int:cita_id>/cancelar/', views.cancelar_cita, name='cancelar_cita'),
    path('citas/hoy/', views.citas_del_dia, name='citas_del_dia'),
]