from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse
from Turnos.models import TipoTurno

class Ticket(View):
	def get(self, request):
		try:
			TipoTurnos = TipoTurno.objects.all()
		except TipoTurnos.DoesNotExist:
			raise Http404("No hay TipoTurnos registrados")
		data = serializers.serialize('json', list(TipoTurnos))
		return HttpResponse(data, content_type='application/json')

	def post(self, request):
		try:
			TipoTurnos = TipoTurno.objects.all()
		except TipoTurnos.DoesNotExist:
			raise Http404("No hay TipoTurnos registrados")
		data = serializers.serialize('json', list(TipoTurnos))
		return HttpResponse(data, content_type='application/json')