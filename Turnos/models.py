from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoTurno(models.Model):

	class Meta:
		verbose_name = "Tipo Turno"
		verbose_name_plural = "Tipo Turnos"

	# Atributos
	TipoTurno = models.CharField(max_length=100)
	IndicativoTurno = models.CharField(max_length=5)

	def __str__(self):
		return self.TipoTurno


class Caja(models.Model):
	class Meta:
		verbose_name = "Caja"
		verbose_name_plural = "Cajas"

	# Atributos
	TipoTurnos = models.ManyToManyField(TipoTurno)
	NumeroCaja = models.IntegerField()
	NombreFuncionario = models.CharField(max_length=100)

	def __str__(self):
		return str(self.NumeroCaja) + " - " + self.NombreFuncionario


class Turno(models.Model):
	class Meta:
		verbose_name = "Turno"
		verbose_name_plural = "Turnos"

	# Atributos
	CodigoTurno = models.CharField(max_length=1000)
	Estado = models.BooleanField()
	Caja = models.ForeignKey(Caja)
	TipoTurno = models.ForeignKey(TipoTurno)
	HoraCreacion = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.CodigoTurno


class Entidad(models.Model):
	class Meta:
		verbose_name = "Entidad"
		verbose_name_plural = "Entidades"

	# Atributos
	Nombre = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
	Tel = models.CharField(max_length=100)
	Url = models.CharField(max_length=1000)

	def __str__(self):
		return self.Nombre
            
    


class Informacion(models.Model):
	class Meta:
		verbose_name = "Informacion"
		verbose_name_plural = "Informaciones"

	Video = models.FileField()
	def __str__(self):
		return str(self.Video)[1:]
    