from django.shortcuts import render
from django.http import HttpResponse
from .models import Almacen


def home(request):
    return HttpResponse('This is my homepage...........')


def index(request):
    almacen = Almacen.objects.get(id=1)
    context = {'almacen':almacen}
    return render(request, 'almacenes/almacen.html', context)



