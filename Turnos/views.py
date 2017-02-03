from django.shortcuts import render
from .models import Informacion


def Pantalla(request):
	i = Informacion.objects.all()
	return render(request, 'pantalla.html', {'Video': i[0]})

# import vistas REST
from Turnos.Vistas.Cajas import Cajas

