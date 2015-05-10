from django.conf.urls import patterns,url

urlpatterns = patterns('pro.apps.home.views',
	url(r'^$','index_formulario',name='vista_formulario'),
	url(r'^agregar_cuestiones/$','index_cuestiones',name='vista_cuestiones'),
	url(r'^respuestas/$','respuestas_view',name='vista_respuestas'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
)
