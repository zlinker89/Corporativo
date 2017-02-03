"""
from django.shortcuts import render,render_to_response, RequestContext, get_object_or_404, redirect, HttpResponse
from django.core import serializers
from django.http import QueryDict
from django.views.generic import View
from .models import Usuario
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	return render_to_response("index.html", context_instance=RequestContext(request))

class Usuarios(View):
	def get(self, request):
		usuarios = Usuario.objects.all()
		data = serializers.serialize('json', list(usuarios))
		return HttpResponse(data, content_type = "application/json")
	
	#@csrf_exempt
	def post(self, request):
		usuario = Usuario(nombre= request.POST.get("nombre"), apellido= request.POST.get("apellido"))
		usuario.save()
		usuario = Usuario.objects.all()#.order_by("-id")[0] # devuelve el ultimo elemento insertado
		data = serializers.serialize('json', usuario)
		return HttpResponse(data, content_type = "application/json")

	def put(self, request):
		print("aver")
		PUT = QueryDict(request.body)
		usuario = Usuario.objects.get(pk=PUT.get("pk"))
		# usuario.update(nombre= PUT.get("nombre"), apellido= PUT.get("apellido"))
		usuario.nombre = PUT.get("nombre")
		usuario.apellido = PUT.get("apellido")
		usuario.save()
		usuario = Usuario.objects.all()#.order_by("-id")[0] # devuelve el ultimo elemento insertado
		data = serializers.serialize('json', usuario)
		return HttpResponse(data, content_type = "application/json")

	def delete(self, request):
		DELETE = QueryDict(request.body)
		pk = DELETE.get('pk')
		Usuario.objects.get(pk= pk).delete()
		return HttpResponse(pk, content_type = "application/json")
		"""