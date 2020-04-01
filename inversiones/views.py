from django.shortcuts import render

from .models import Inversion



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