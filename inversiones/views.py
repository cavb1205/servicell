from django.shortcuts import render,redirect

from .models import Inversion
from .forms import InversionForm



def inversion_list(request):
    """vista de la lista de inversiones"""

    inversion_list = Inversion.objects.all()
    context = {'inversion_list': inversion_list}
    return render(request, 'inversiones/inversion_list.html', context)


def inversion_detail(request, inversion_id):
    """vista de inversion detail"""

    inversion = Inversion.objects.get(id=inversion_id)
    context = {'inversion':inversion}
    return render(request,'inversiones/inversion_detail.html', context)


def inversion_create(request):
    """vista para crear un nuevo resgistro de inversion"""

    if request.method == 'POST':
        form = InversionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inversion/')
    else:
        form = InversionForm()
    return render(request, 'inversiones/inversion_form.html', {'form':form})


def inversion_update(request, inversion_id):
    inversion = Inversion.objects.get(id=inversion_id)
    if request.method == 'POST':
        form = InversionForm(request.POST, instance=inversion)
        if form.is_valid():
            form.save()
            return redirect('/inversion/')
    else:
        form = InversionForm(instance=inversion)
    return render(request, 'inversiones/inversion_form.html', {'form':form})



def inversion_delete(request, inversion_id):
    """vista para eliminar un registro de inversion"""

    inversion = Inversion.objects.get(id=inversion_id)
    inversion.delete()
    return redirect('/inversion/')