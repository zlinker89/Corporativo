from django.shortcuts import render
from .models import Informacion


def Pantalla(request):
	i = Informacion.objects.all()
	return render(request, 'pantalla.html', {'Video': i[0]})


def TipoTurnos(request):
	return render(request, 'ticket.html')

# import vistas REST
from Turnos.Vistas.Cajas import Cajas
from Turnos.Vistas.Ticket import Ticket

