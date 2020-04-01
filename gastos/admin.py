from django.contrib import admin

from .models import Gasto, Tipo_Gasto

admin.site.register(Tipo_Gasto)
admin.site.register(Gasto)
