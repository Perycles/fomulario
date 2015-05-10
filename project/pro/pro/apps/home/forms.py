from django import forms
from pro.apps.formularios.models import Datos_personales
from pro.apps.formularios.models import Cuestiones
from localflavor.es.forms import *
from localflavor.es.forms import ESPhoneNumberField
from localflavor.es.forms import ESIdentityCardNumberField
from localflavor.es.forms import ESPostalCodeField
from localflavor.es.forms import ESProvinceSelect

class ContactForm(forms.Form):
	Nombre			= forms.CharField(widget=forms.TextInput())
	Primer_Apellido		= forms.CharField(widget=forms.TextInput())
	Segundo_Apellido	= forms.CharField(widget=forms.TextInput())
	Fecha_de_Nacimiento	= forms.DateField()
	DNI			= ESIdentityCardNumberField(max_length=9)
	Provincia		= forms.ChoiceField(widget=ESProvinceSelect(), choices=(
		('1','Almeria'),('2','Cadiz'),('3','Cordoba'),('4','Granada'),('5','Huelva'),
		('6','Jaen'),('7','Malaga'),('8','Sevilla')))

	Codigo_Postal		= ESPostalCodeField(max_length=5)
	Telefono		= ESPhoneNumberField(max_length=9)
	Movil			= forms.DecimalField(widget=forms.TextInput())
	Email			= forms.EmailField(label='Email')
	Estudios_anteriores 	= forms.CharField(widget=forms.TextInput())
	Observaciones		= forms.CharField(widget=forms.TextInput(attrs={'size':'70'}))

	def clean(self):
		return self.cleaned_data

class Cuestionario(forms.Form):
	Cuestion	= forms.CharField(widget=forms.Textarea())

	def clean(self):
		return self.cleaned_data

class Resp(forms.Form):
	Respuesta 	= forms.CharField(widget=forms.Textarea())

	def clean(self):
		return self.cleaned_data

class LoginForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput())
	password	= forms.CharField(widget=forms.PasswordInput(render_value=False))
