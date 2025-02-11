from django.db import models
from django.core.validators import RegexValidator

# Validador para permitir solo letras y espacios en nombres
solo_letras = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', "Solo se permiten letras y espacios.")

# Validador para permitir solo números en teléfono
solo_numeros = RegexValidator(r'^\d+$', "Solo se permiten números.")

class Constructora(models.Model):
    nombre = models.CharField(max_length=200, validators=[solo_letras])
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, validators=[solo_numeros])
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class ProyectoInfraestructura(models.Model):
    nombre = models.CharField(max_length=255, validators=[solo_letras])
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Carretera(models.Model):
    nombre = models.CharField(max_length=255, validators=[solo_letras])
    longitud_km = models.DecimalField(max_digits=10, decimal_places=2, validators=[solo_numeros])
    tipo_superficie = models.CharField(max_length=100, validators=[solo_letras])
    proyecto = models.ForeignKey(ProyectoInfraestructura, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    proyecto = models.ForeignKey(ProyectoInfraestructura, on_delete=models.CASCADE)
    monto_estimado = models.DecimalField(max_digits=12, decimal_places=2)
    monto_real = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fecha_aprobacion = models.DateField()

    def __str__(self):
        return f"{self.proyecto.nombre} - ${self.monto_estimado}"
