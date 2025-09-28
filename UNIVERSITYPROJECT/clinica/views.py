# views.py - Corregido para tu estructura de BD

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Pacientes, Medicos, Citas, Especialidades, Consultorios
from .forms import PacienteForm, CitaForm
from datetime import date, datetime

def home(request):
    """Página de inicio con estadísticas generales"""
    total_pacientes = Pacientes.objects.count()
    total_medicos = Medicos.objects.count()
    total_citas = Citas.objects.count()
    citas_hoy = Citas.objects.filter(fecha_cita=date.today()).exclude(estado='CANCELADA').count()
    
    # Citas próximas (siguiente semana)
    from datetime import timedelta
    proxima_semana = date.today() + timedelta(days=7)
    citas_proximas = Citas.objects.filter(
        fecha_cita__range=[date.today(), proxima_semana]
    ).select_related('id_paciente', 'id_medico').order_by('fecha_cita', 'hora_cita')[:5]
    
    context = {
        'total_pacientes': total_pacientes,
        'total_medicos': total_medicos,
        'total_citas': total_citas,
        'citas_hoy': citas_hoy,
        'citas_proximas': citas_proximas,
    }
    return render(request, 'clinica/home.html', context)

def listar_pacientes(request):
    """Lista todos los pacientes"""
    pacientes = Pacientes.objects.all().order_by('apellido', 'nombre')
    return render(request, 'clinica/listar_pacientes.html', {'pacientes': pacientes})

def agregar_paciente(request):
    """Agregar nuevo paciente"""
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Paciente agregado exitosamente')
                return redirect('listar_pacientes')
            except Exception as e:
                messages.error(request, f'Error al agregar paciente: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = PacienteForm()
    
    return render(request, 'clinica/agregar_paciente.html', {'form': form})

def listar_citas(request):
    """Lista todas las citas con contadores"""
    from django.utils import timezone
    hoy = timezone.localdate()

    qs = Citas.objects.select_related(
        'id_paciente',
        'id_medico',
        'id_medico__id_especialidad',
        'id_consultorio'
    )

    total_citas = qs.exclude(estado='CANCELADA').count()
    confirmadas = qs.filter(estado='CONFIRMADA').count()
    pendientes = qs.filter(estado__in=['PROGRAMADA', 'REPROGRAMADA']).count()
    hoy_count  = qs.filter(fecha_cita=hoy).exclude(estado='CANCELADA').count()

    citas = qs.order_by('-fecha_cita', '-hora_cita')

    context = {
        'citas': citas,
        'total_citas': total_citas,
        'confirmadas': confirmadas,
        'pendientes': pendientes,
        'hoy_count': hoy_count,
    }
    return render(request, 'clinica/listar_citas.html', context)


def agregar_cita(request):
    """Agregar nueva cita"""
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            try:
                # Validar que la fecha no sea en el pasado
                fecha_cita = form.cleaned_data['fecha_cita']
                if fecha_cita < date.today():
                    messages.error(request, 'No se pueden programar citas en fechas pasadas')
                    return render(request, 'clinica/agregar_cita.html', {'form': form})
                
                # Verificar disponibilidad del médico
                medico = form.cleaned_data['id_medico']
                hora_cita = form.cleaned_data['hora_cita']
                
                cita_existente = Citas.objects.filter(
                    id_medico=medico,
                    fecha_cita=fecha_cita,
                    hora_cita=hora_cita
                ).exclude(estado='CANCELADA').exists()
                
                if cita_existente:
                    messages.error(request, 'El médico ya tiene una cita programada en ese horario')
                    return render(request, 'clinica/agregar_cita.html', {'form': form})
                
                # Guardar la cita
                cita = form.save(commit=False)
                cita.estado = 'PROGRAMADA'
                cita.save()
                
                messages.success(request, 'Cita programada exitosamente')
                return redirect('listar_citas')
                
            except Exception as e:
                messages.error(request, f'Error al programar cita: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = CitaForm()
    
    return render(request, 'clinica/agregar_cita.html', {'form': form})

def detalle_paciente(request, paciente_id):
    """Ver detalles de un paciente"""
    paciente = get_object_or_404(Pacientes, id_paciente=paciente_id)
    citas_paciente = Citas.objects.filter(id_paciente=paciente).select_related(
        'id_medico', 'id_medico__id_especialidad'
    ).order_by('-fecha_cita', '-hora_cita')
    
    context = {
        'paciente': paciente,
        'citas': citas_paciente
    }
    return render(request, 'clinica/detalle_paciente.html', context)

def cancelar_cita(request, cita_id):
    """Cancelar una cita"""
    if request.method == 'POST':
        cita = get_object_or_404(Citas, id_cita=cita_id)
        cita.estado = 'CANCELADA'
        cita.save()
        messages.success(request, 'Cita cancelada exitosamente')
    
    return redirect('listar_citas')

def citas_del_dia(request):
    """Ver citas del día actual"""
    hoy = date.today()
    citas_hoy = Citas.objects.filter(fecha_cita=hoy).select_related(
        'id_paciente', 'id_medico', 'id_consultorio'
    ).exclude(estado='CANCELADA').order_by('hora_cita')
    
    return render(request, 'clinica/citas_del_dia.html', {
        'citas': citas_hoy,
        'fecha': hoy
    })

def listar_medicos(request):
    """Lista todos los médicos"""
    medicos = Medicos.objects.select_related('id_especialidad').all().order_by('apellido', 'nombre')
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def agregar_medico(request):
    """Agregar nuevo médico"""
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            cedula_profesional = request.POST.get('cedula_profesional')
            especialidad_id = request.POST.get('especialidad')
            
            # Validar campos obligatorios
            if not all([nombre, apellido, cedula_profesional, especialidad_id]):
                messages.error(request, 'Todos los campos son obligatorios')
                return redirect('agregar_medico')
            
            # Crear nuevo médico
            nuevo_medico = Medicos(
                nombre=nombre,
                apellido=apellido,
                cedula_profesional=cedula_profesional,
                id_especialidad_id=especialidad_id
            )
            nuevo_medico.save()
            messages.success(request, 'Médico agregado exitosamente')
            return redirect('listar_medicos')
            
        except Exception as e:
            messages.error(request, f'Error al agregar médico: {str(e)}')
    
    especialidades = Especialidades.objects.all().order_by('nombre_especialidad')
    return render(request, 'clinica/agregar_medico.html', {'especialidades': especialidades})

def detalle_medico(request, medico_id):
    """Ver detalles de un médico"""
    medico = get_object_or_404(Medicos, id_medico=medico_id)
    citas_medico = Citas.objects.filter(id_medico=medico).select_related(
        'id_paciente'
    ).order_by('-fecha_cita', '-hora_cita')[:10]  # Últimas 10 citas
    
    context = {
        'medico': medico,
        'citas': citas_medico
    }
    return render(request, 'clinica/detalle_medico.html', context)