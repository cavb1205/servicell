from django.shortcuts import render
from django.http import HttpResponse
from .models import Almacen


def home(request):
    return render(request, 'almacenes/base.html')


def index(request):
    almacen = Almacen.objects.get(id=1)
    context = {'almacen':almacen}
    return render(request, 'almacenes/almacen.html', context)



