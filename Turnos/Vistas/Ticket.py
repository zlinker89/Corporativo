from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, Http404
from Turnos.models import TipoTurno, Turno
import json, ast
class Ticket(View):
	def get(self, request):
		try:
			TipoTurnos = TipoTurno.objects.all()
		except TipoTurnos.DoesNotExist:
			raise Http404("No hay TipoTurnos registrados")
		data = serializers.serialize('json', list(TipoTurnos))
		return HttpResponse(data, content_type='application/json')

	def post(self, request):
		"""
			hubo un error entre angular y django TENER ENCUENTA
		"""
		t = None
		print "---------------------------------------"
		for key in ast.literal_eval(json.dumps(request.POST.dict())):
			tipo = TipoTurno.objects.get(pk=int(key))
			print tipo
			NumeroCurso = Turno.objects.filter(TipoTurno= tipo.pk).order_by('-pk')
			if NumeroCurso:
				NumeroCurso = int(NumeroCurso[0].CodigoTurno[1:]) + 1
				if NumeroCurso > 999:
					NumeroCurso = 01
			else:
				NumeroCurso = 01;
			t = Turno(CodigoTurno= tipo.IndicativoTurno + str(NumeroCurso),TipoTurno = tipo, Estado = True)
			if not self.TurnoInDB(tipo.IndicativoTurno + str(NumeroCurso)):
				t.save()
			print tipo.IndicativoTurno + str(NumeroCurso)
		print "---------------------------------------"
		
		return HttpResponse(t.CodigoTurno)




	def TurnoInDB(self, CodigoTurno):
		t = Turno.objects.filter(CodigoTurno = CodigoTurno, Estado = True)
		if t.count() > 0:
			return True
		else:
			return False
