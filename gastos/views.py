from django.shortcuts import render,redirect

from .models import Gasto, Tipo_Gasto
from .forms import GastoForm, Tipo_GastoForm



def gasto_list(request):
    """vista de la lista de gastos"""

    gasto_list = Gasto.objects.all()
    context = {'gasto_list': gasto_list}
    return render(request, 'gastos/gasto_list.html', context)


def gasto_detail(request, gasto_id):
    """vista de gasto detail"""

    gasto = Gasto.objects.get(id=gasto_id)
    context = {'gasto':gasto}
    return render(request,'gastos/gasto_detail.html', context)


def gasto_create(request):
    """vista para crear un nuevo resgistro de gasto"""

    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gasto/')
    else:
        form = GastoForm()
    return render(request, 'gastos/gasto_form.html', {'form':form})


def gasto_update(request, gasto_id):
    gasto = Gasto.objects.get(id=gasto_id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('/gasto/')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'gastos/gasto_form.html', {'form':form})



def gasto_delete(request, gasto_id):
    """vista para eliminar un registro de gasto"""

    gasto = Gasto.objects.get(id=gasto_id)
    gasto.delete()
    return redirect('/gasto/')