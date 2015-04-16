from django.conf.urls import include, url 
from django.contrib import admin
from site_test.views import hola, fecha_actual, horas_adelante


urlpatterns = [ 
	url(r'^admin/', include('django.contrib.admin.urls')),
	url(r'^hola/$',hola),
	url(r'^fecha/$',fecha_actual),
	url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
]
