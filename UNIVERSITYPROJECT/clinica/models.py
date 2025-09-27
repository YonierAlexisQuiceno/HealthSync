from django.db import models

class Especialidades(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=100)

    class Meta:
        managed = False  # No permitir que Django modifique la tabla
        db_table = 'especialidades'
    
    def __str__(self):
        return self.nombre_especialidad

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'pacientes'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    @property
    def edad(self):
        if self.fecha_nacimiento:
            from datetime import date
            today = date.today()
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula_profesional = models.CharField(unique=True, max_length=20)
    id_especialidad = models.ForeignKey(Especialidades, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'medicos'
    
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

class Consultorios(models.Model):
    id_consultorio = models.AutoField(primary_key=True)
    numero_consultorio = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'consultorios'
    
    def __str__(self):
        return f"Consultorio {self.numero_consultorio}"

class Citas(models.Model):
    ESTADOS_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('CONFIRMADA', 'Confirmada'),
        ('EN_CURSO', 'En Curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No Asistió'),
    ]
    
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Pacientes', models.DO_NOTHING, db_column='id_paciente')
    id_medico = models.ForeignKey('Medicos', models.DO_NOTHING, db_column='id_medico')
    id_consultorio = models.ForeignKey('Consultorios', models.DO_NOTHING, db_column='id_consultorio')
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='PROGRAMADA')
    motivo_consulta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citas'
        ordering = ['-fecha_cita', '-hora_cita']
    
    def __str__(self):
        return f"Cita {self.id_paciente.nombre} {self.id_paciente.apellido} - {self.fecha_cita} {self.hora_cita}"