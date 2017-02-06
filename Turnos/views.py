from django.shortcuts import render, render_to_response, redirect
from .models import Informacion, Entidad, UsuarioCaja, Turno, TipoTurno, Entidad
from django.http import HttpResponse
from django.core import serializers
from itertools import chain



def Pantalla(request):
	try:
		i = Informacion.objects.all()
	except i.DoesNotExist:
		raise Http404("No hay videos")
	return render(request, 'pantalla.html', {'Video': i[0]})


def TipoTurnos(request):
	return render(request, 'ticket.html')


def Index(request):
	return render(request, 'index.html')


def CajaUsuario(request):
	# verificamos el usuario
	u = UsuarioCaja.objects.filter(pk=int(request.session.get("usuario")))
	if(len(u) == 0):
		return redirect("/logout")
	usuario = u[0]
	# TurnosEspera = None
	# TurnoActivo = Turno.objects.filter(Estado=True, Caja = u[0].Caja)
	# if TurnoActivo.count() > 0:
	# 	TurnoActivo = TurnoActivo[0]
	# 	TurnoActivo.Llamados -= 1
	# for t in u[0].Caja.TipoTurnos.all():
	# 	Turnos = Turno.objects.filter(Estado=True, TipoTurno= t, Caja=None)
	# 	if not TurnosEspera:
	# 		TurnosEspera = Turnos
	# 	else:
	# 		TurnosEspera = chain(TurnosEspera, Turnos)
	return render_to_response("Caja.html",locals())


def TurnosEspera(request):
	# verificamos el usuario
	u = UsuarioCaja.objects.filter(pk=int(request.session.get("usuario")))
	if(len(u) == 0):
		return redirect("/logout")
	usuario = u[0]
	TurnosEspera = None
	for t in u[0].Caja.TipoTurnos.all():
		Turnos = Turno.objects.filter(Estado=True, TipoTurno= t, Caja=None)
		if not TurnosEspera:
			TurnosEspera = Turnos
		else:
			TurnosEspera = chain(TurnosEspera, Turnos)
	data = serializers.serialize('json', list(TurnosEspera))
	return HttpResponse(data, content_type='application/json')


def TurnoActivo(request):
	# verificamos el usuario
	u = UsuarioCaja.objects.filter(pk=int(request.session.get("usuario")))
	if(len(u) == 0):
		return redirect("/logout")
	usuario = u[0]
	TurnoActivo = Turno.objects.filter(Estado=True, Caja = u[0].Caja)
	if TurnoActivo.count() > 0:
		TurnoActivo[0].Llamados -= 1
	data = serializers.serialize('json', list(TurnoActivo))
	return HttpResponse(data, content_type='application/json')


def Llamar(request, idTurno):
	# verificamos el usuario
	u = UsuarioCaja.objects.filter(pk=int(request.session.get("usuario")))
	if(len(u) == 0):
		return redirect("/logout")
	t = Turno.objects.get(pk=idTurno)
	TurnoPendiente = Turno.objects.filter(Estado=True, Caja=u[0].Caja)
	if TurnoPendiente.count() != 0:
		t = TurnoPendiente[0]
	if t.Caja == None:
		t.Caja = u[0].Caja
		t.save()
	elif t.Caja == u[0].Caja and t.Llamados > 0:
		t.Llamados -= 1
		if t.Llamados <= 0:
			t.Estado = False
		t.save()
	data = serializers.serialize('json', list(TurnoPendiente))
	return HttpResponse(data, content_type='application/json')


def Finalizar(request, idTurno):
	# verificamos el usuario
	u = UsuarioCaja.objects.filter(pk=int(request.session.get("usuario")))
	if(len(u) == 0):
		return redirect("/logout")
	t = Turno.objects.get(Estado=True, Caja=u[0].Caja)
	t.Llamados = 0
	t.Estado = False
	t.save()
	data = serializers.serialize('json', list(u))
	return HttpResponse(data, content_type='application/json')


def PantallaLogica(request):
	TurnosEspera = None
	tipos = TipoTurno.objects.all()
	for t in tipos:
		Turnos = Turno.objects.filter(Estado=True, TipoTurno= t).exclude(Caja=None)
		if not TurnosEspera:
			TurnosEspera = Turnos
		else:
			TurnosEspera = chain(TurnosEspera, Turnos)
	data = serializers.serialize('json', list(TurnosEspera))
	return HttpResponse(data, content_type='application/json')


def login(request):
	try:
		if(request.method == 'POST'):
			
			u = UsuarioCaja.objects.filter(Nombre = request.POST.get("Nombre"),Password = request.POST.get("Password"))
			if len(u) > 0:
				request.session['usuario'] = u[0].pk
				return redirect("CajaUsuario")
			else:
				error = "Nombre o contrasena invalidos."
				return render_to_response("index.html",locals())
	except Exception as e:
		redirect("Index")


def logout(request):
	request.session['usuario'] = -1
	return redirect("Index")


def Entidades(request):
	Elst = Entidad.objects.all()
	data = serializers.serialize('json', list(Elst))
	return HttpResponse(data, content_type='application/json')


# import vistas REST
from Turnos.Vistas.Cajas import Cajas
from Turnos.Vistas.Ticket import Ticket

