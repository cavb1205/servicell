from django.shortcuts import render,redirect

from .models import Utilidad
from .forms import UtilidadForm




def utilidad_list(request):
    """vista de la lista de utilidades"""

    utilidad_list = Utilidad.objects.all()
    context = {'utilidad_list': utilidad_list}
    return render(request, 'utilidades/utilidad_list.html', context)


def utilidad_detail(request, utilidad_id):
    """vista de utilidad detail"""

    utilidad = Utilidad.objects.get(id=utilidad_id)
    context = {'utilidad':utilidad}
    return render(request,'utilidades/utilidad_detail.html', context)


def utilidad_create(request):
    """vista para crear un nuevo resgistro de utilidad"""

    if request.method == 'POST':
        form = UtilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/utilidad/')
    else:
        form = UtilidadForm()
    return render(request, 'utilidades/utilidad_form.html', {'form':form})


def utilidad_update(request, utilidad_id):
    utilidad = Utilidad.objects.get(id=utilidad_id)
    if request.method == 'POST':
        form = UtilidadForm(request.POST, instance=utilidad)
        if form.is_valid():
            form.save()
            return redirect('/utilidad/')
    else:
        form = UtilidadForm(instance=utilidad)
    return render(request, 'utilidades/utilidad_form.html', {'form':form})



def utilidad_delete(request, utilidad_id):
    """vista para eliminar un registro de utilidad"""

    utilidad = Utilidad.objects.get(id=utilidad_id)
    utilidad.delete()
    return redirect('/utilidad/')