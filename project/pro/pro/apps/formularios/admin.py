from django.contrib import admin
from pro.apps.formularios.models import Cuestiones,Respuestas,Datos_personales

# Register your models here.

admin.site.register(Cuestiones)
admin.site.register(Respuestas)
admin.site.register(Datos_personales)
