from django.shortcuts import render
from .models import Informacion, Entidad


def Entidad(request):
	pass

	
def Pantalla(request):
	try:
		i = Informacion.objects.all()
	except i.DoesNotExist:
		raise Http404("No hay videos")
	return render(request, 'pantalla.html', {'Video': i[0]})


def TipoTurnos(request):
	return render(request, 'ticket.html')

# import vistas REST
from Turnos.Vistas.Cajas import Cajas
from Turnos.Vistas.Ticket import Ticket

