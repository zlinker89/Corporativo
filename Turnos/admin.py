from django.contrib import admin
from .models import TipoTurno
from .models import Turno
from .models import Caja
from .models import Entidad
from .models import Informacion

# Register your models here.

admin.site.register(TipoTurno)
admin.site.register(Turno)
admin.site.register(Caja)
admin.site.register(Entidad)
admin.site.register(Informacion)