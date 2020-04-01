from django.forms import ModelForm

from .models import Utilidad


class UtilidadForm(ModelForm):
    class Meta:
        model = Utilidad
        fields = '__all__'