import datetime
#from django.http import HttpResponse
from django.shortcuts import render



def hola(request):
	salida = "Hola Mundo!"
	return render(request,'aplicacion/hola.html',{'hola':salida})
	#'aplicacion/hola.html' es para ubicar el .html 
	# el {'hola':salida} indica que 'hola' es la variable que esta en el html y 'salida' es el valor que se le va asignar

def fecha_actual(request):
	ahora = datetime.datetime.now()
	return render(request,'fecha_actual.html',{'fecha_actual': ahora})

def horas_adelante(request, horas): 
	try:
		horas = int(horas) 
	except ValueError:
		raise Http404()
	dt= datetime.datetime.now()+datetime.timedelta(hours=horas) 
	
	return render(request,'horas_adelante.html',{'hora_siguiente':dt,'horas':horas})
	#'hora_siguiente' es la variable que esta en horas_adelante.html y 'dt' es el valor a asignar


