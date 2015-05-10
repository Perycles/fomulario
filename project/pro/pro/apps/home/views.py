from django.shortcuts import render_to_response
from django.template import RequestContext
from pro.apps.home.forms import ContactForm, LoginForm
from pro.apps.formularios.models import Datos_personales
from pro.apps.formularios.models import Cuestiones
from pro.apps.home.forms import Cuestionario
from pro.apps.home.forms import Resp

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

# Create your views here.

def index_formulario(request):
	info_enviado		= False
	Nombre			= ""
	Primer_Apellido		= ""
	Segundo_Apellido 	= ""
	Fecha_de_Nacimiento 	= ""
	DNI 			= ""
	Provincia		= ""
	Codigo_Postal		= ""
	Telefono		= ""
	Movil			= ""
	Email		 	= ""
	Estudios_anteriores 	= ""
	Observaciones		= ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		info2 = "Iniciando"
		if formulario.is_valid():
			info_enviado = True
			Nombre			= formulario.cleaned_data['Nombre']
			Primer_Apellido		= formulario.cleaned_data['Primer_Apellido']
			Segundo_Apellido	= formulario.cleaned_data['Segundo_Apellido']
			Fecha_de_Nacimiento	= formulario.cleaned_data['Fecha_de_Nacimiento']
			DNI			= formulario.cleaned_data['DNI']
			Provincia		= formulario.cleaned_data['Provincia']
			Codigo_Postal		= formulario.cleaned_data['Codigo_Postal']
			Telefono		= formulario.cleaned_data['Telefono']
 			Movil			= formulario.cleaned_data['Movil']
 			Email			= formulario.cleaned_data['Email']
 			Estudios_anteriores	= formulario.cleaned_data['Estudios_anteriores']
 			Observaciones		= formulario.cleaned_data['Observaciones']
			dp			= Datos_personales()
			dp.Nombre		= Nombre
			dp.Primer_Apellido	= Primer_Apellido
			dp.Segundo_Apellido	= Segundo_Apellido
			dp.Fecha_de_Nacimiento	= Fecha_de_Nacimiento
			dp.DNI			= DNI
			dp.Provincia		= Provincia
			dp.Codigo_Postal	= Codigo_Postal
			dp.Telefono		= Telefono
			dp.Movil		= Movil
			dp.Email		= Email
			dp.Estudios_anteriores	= Estudios_anteriores
			dp.Observaciones	= Observaciones
			dp.save() #Guarda la informacion
			info2 = "Los datos se han guardado correctamente"
		else:
			info2 = "Datos incorrectos"
		formulario = ContactForm()
		respuestas = Cuestiones.objects.filter(status=True)
		respu = Resp()
		ctx = {'form':formulario, 'info2':info2,'respuest':respuestas,'res':respu}
		return render_to_response('home/respuestas.html',ctx,context_instance=RequestContext(request))
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'Nombre':Nombre,'Primer_Apellido':Primer_Apellido,
		'Segundo_Apellido':Segundo_Apellido,'Fecha_de_Nacimiento':Fecha_de_Nacimiento,
		'DNI':DNI,'Provincia':Provincia,'Codigo_Postal':Codigo_Postal,'Telefono':Telefono,
		'Movil':Movil,'Email':Email,
		'Estudios_anteriores':Estudios_anteriores,'Observaciones':Observaciones,
		'info_enviado':info_enviado}
	return render_to_response('home/formulario1.html',ctx,context_instance=RequestContext(request))

def index_cuestiones(request):
	cue = Cuestiones.objects.filter(status=True)
	info_enviado = False
	Cuestion = ""
	if request.user.is_authenticated():
		if request.method == "POST":
			cuesti = Cuestionario(request.POST)
			info = "Inicializando"
			if cuesti.is_valid():
				info_enviado = True
				Cuestion = cuesti.cleaned_data['Cuestion']
				c = Cuestiones()
				c.Cuestion = Cuestion
				c.status = True
				c.save()
				info = "La/s cuestion/es se guardaron correctamente"
			else:
				info = "Datos incorrectos"
			cuesti = Cuestionario()
			respu = Resp()
			ctx = {'cuestionario':cuesti,'informacion':info,'cues':cue}
			return render_to_response('home/cuestiones.html',ctx,context_instance=RequestContext(request))
		else:
			cuesti = Cuestionario()
			respu = Resp()
			ctx = {'cuestionario':cuesti,'Cuestion':Cuestion,'info_enviado':info_enviado,'cues':cue}
			return render_to_response('home/cuestiones.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

"""def cuestiones_view(request):
	cue = Cuestiones.objects.filter(status=True)
	ctx = {'cues':cue}
#	print cue
	return render_to_response('home/cuestiones.html',ctx,context_instance=RequestContext(request))
"""

def respuestas_view(request):
	respuestas = Cuestiones.objects.filter(status=True)
	respu = Resp()
	ctx = {'respuest':respuestas,'res':respu}
	return render_to_response('home/respuestas.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "Usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
