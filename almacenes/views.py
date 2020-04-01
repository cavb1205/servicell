from django.shortcuts import render
from django.http import HttpResponse
from .models import Almacen


def home(request):
    """vista de la pagina principal"""

    return render(request, 'home.html')


def almacen_detail(request, almacen_id):
    """vista detalle del almacen"""

    almacen = Almacen.objects.get(id=almacen_id)
    context = {'almacen':almacen}
    return render(request, 'almacenes/almacen_detail.html', context)


