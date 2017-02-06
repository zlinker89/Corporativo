"""Corporativo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Turnos import views
from Corporativo import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cajas/', views.Cajas.as_view(), name='Cajas'),
    url(r'^Ticket/', views.Ticket.as_view(), name='Ticket'),
    url(r'^tipoturnos/', views.TipoTurnos, name='TipoTurnos'),
    url(r'^pantalla/', views.Pantalla, name='Pantalla'),
    url(r'^logica/', views.PantallaLogica, name='PantallaLogica'),
    url(r'^login/', views.login, name='login'),
    url(r'^cajausuario/', views.CajaUsuario, name='CajaUsuario'),
    url(r'^llamar/(/*[0-9]+)/', views.Llamar, name='Llamar'),
    url(r'^finalizar/(/*[0-9]+)/', views.Finalizar, name='Finalizar'),
    url(r'^turnosespera/', views.TurnosEspera, name='TurnosEspera'),
    url(r'^turnoactivo/', views.TurnoActivo, name='TurnoActivo'),
    url(r'^entidad/', views.Entidades, name='Entidades'),
    url(r'^$', views.Index, name='Index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)