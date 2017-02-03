from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse
from Turnos.models import Caja

class Cajas(View):
	def get(self, request):
		return HttpResponse("Error")

	def post(self, request):
		try:
			Cajas = Caja.objects.all()
		except Cajas.DoesNotExist:
			raise Http404("No hay cajas registradas")
		data = serializers.serialize('json', list(Cajas))
		return HttpResponse(data, content_type='application/json')
