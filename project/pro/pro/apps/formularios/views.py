#from django.shortcuts import render_to_response
#from django.templates import RequestContext
#from django.http import HttpResponseRedirect

# Create your views here.

#def add_alumno_view(request):
#	info = "Iniciado"
#	if request.method == "POST"
#		form = addAlumnoForm(request.POST,request.FILES)
#		if form.is_valid():
#			add = form.save(commit=False)
#			add.status = True
#			add.save()
#			info = "Guardado satisfactoriamente"
#			return HttpResponseRedirect('/datos_personales/%s'%add.id)
#	else:
#		form = addAlumnoForm()
#	ctx = {'form':form,'informacion':info}
#
#	return render_to_response('formulario/addAlumno.html',ctx,context_instance=RequestContext(request))


