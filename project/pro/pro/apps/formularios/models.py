from django.db import models

# Create your models here.

class Cuestiones(models.Model):
	Cuestion	= models.TextField(max_length=400)
#	respuesta	= models.OneToOneField(Respuestas,primary_key=True)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		return self.Cuestion

class Respuestas(models.Model):
#	Nombre		= models.CharField(max_length=200)
	dat_per 	= models.ForeignKey('Datos_personales')
	cuestion 	= models.ForeignKey('Cuestiones')
	Respuesta	= models.TextField(max_length=400)

	def __unicode__(self):
		respu = "%s  %s"%(self.dat_per,self.Respuesta)
		return respu

class Datos_personales(models.Model):
	Nombre			= models.CharField(max_length=30)
	Primer_Apellido		= models.CharField(max_length=60)
	Segundo_Apellido 	= models.CharField(max_length=60)
	Fecha_de_Nacimiento 	= models.DateTimeField()
	DNI 			= models.CharField(unique=True, max_length=10)
	Provincia		= models.CharField(max_length=50)
	Codigo_Postal		= models.CharField(max_length=10)
	Telefono		= models.CharField(unique=True, max_length=20)
	Movil			= models.CharField(unique=True, max_length=20)
	Email 			= models.EmailField()
	Estudios_anteriores 	= models.CharField(max_length=300)
	Observaciones 		= models.CharField(max_length=400)
#	cuestion 		= models.OneToOneField(Cuestiones,primary_key=True)
#	respuesta 		= models.OneToOneField(Respuestas)
	status			= models.BooleanField(default=True)

	def __unicode__(self):
		nombreCompleto = "%s  %s  %s"%(self.Nombre,self.Primer_Apellido,self.Segundo_Apellido)
		return nombreCompleto
