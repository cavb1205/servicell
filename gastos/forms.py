from django.forms import ModelForm

from .models import Gasto, Tipo_Gasto


class Tipo_GastoForm(ModelForm):
    class Meta:
        model = Tipo_Gasto
        fields = '__all__'


class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'