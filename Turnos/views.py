from django.shortcuts import render
from .models import Caja


def Pantalla(request):
	return render(request, 'pantalla.html')

# import vistas REST
from Turnos.Vistas.Cajas import Cajas

