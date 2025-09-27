from django import forms
from .models import Pacientes, Citas, Medicos, Consultorios, Especialidades

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes 
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3001234567'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Citas 
        fields = ['id_paciente', 'id_medico', 'id_consultorio', 'fecha_cita', 'hora_cita', 'motivo_consulta']
        widgets = {
            'id_paciente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_medico': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_consultorio': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_cita': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'hora_cita': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'motivo_consulta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describa el motivo de la consulta'
            }),
        }
        labels = {
            'id_paciente': 'Paciente',
            'id_medico': 'Médico',
            'id_consultorio': 'Consultorio',
            'fecha_cita': 'Fecha de la Cita',
            'hora_cita': 'Hora de la Cita',
            'motivo_consulta': 'Motivo de Consulta',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los querysets para mostrar mejor información
        self.fields['id_paciente'].queryset = Pacientes.objects.all().order_by('apellido', 'nombre')
        self.fields['id_medico'].queryset = Medicos.objects.select_related('id_especialidad').order_by('apellido', 'nombre')
        self.fields['id_consultorio'].queryset = Consultorios.objects.all().order_by('numero_consultorio')
        
        # Personalizar cómo se muestran las opciones
        self.fields['id_paciente'].empty_label = "Seleccione un paciente"
        self.fields['id_medico'].empty_label = "Seleccione un médico"
        self.fields['id_consultorio'].empty_label = "Seleccione un consultorio"

# Formulario para búsquedas
class BuscarPacienteForm(forms.Form):
    busqueda = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre, apellido o correo...'
        })
    )

class FiltrarCitasForm(forms.Form):
    ESTADO_CHOICES = [
        ('', 'Todos los estados'),
        ('PROGRAMADA', 'Programada'),
        ('CONFIRMADA', 'Confirmada'),
        ('EN_CURSO', 'En Curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No Asistió'),
    ]
    
    fecha_desde = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    fecha_hasta = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    estado = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    medico = forms.ModelChoiceField(
        queryset=Medicos.objects.all().order_by('apellido', 'nombre'),
        required=False,
        empty_label="Todos los médicos",
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )