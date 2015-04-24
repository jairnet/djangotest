from django.conf.urls import url, include
from django.contrib import admin #Esta linea invoca todas las vistas que tiene el modulo admin
from biblioteca import views # Con esta Linea se importan todas las vistas que esten dentro de esta aplicacion biblioteca
from contactos.views import contactos
from site_test.views import hola, fecha_actual, horas_adelante # Es la forma de llamar las funciones locales del archivo views.py del proyecto


urlpatterns = [ 
	url(r'^admin/',include(admin.site.urls)),
	url(r'^hola/$',hola),
	url(r'^fecha/$',fecha_actual), #^fecha es la url de la pagina y "fecha_actual" es la funcion que esta en el archivo views.py
	url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
	url(r'^formulario_buscar/$', views.formulario_buscar),
	url(r'^buscar/$',views.buscar),
	url(r'^contactos/$',contactos),
	#url(r'^gracias/$',gracias),
	#url(r'^resultados/$',views.resultados),
]
