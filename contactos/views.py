from django.shortcuts import render
from contactos.forms import FormularioContactos
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def contactos(request):
	if request.method == 'POST':
		form = FormularioContactos(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['asunto'],
				cd['mensaje'],
				cd.get('email','jairnet5@gmail.com'),
				['jairnet5@hotmail.com'],
			)
			#return HttpResponseRedirect('contactos/gracias.html')
			return render(request,'gracias.html')
	else:
		form = FormularioContactos()
	return render(request,'contactos.html',{'form':form})
		