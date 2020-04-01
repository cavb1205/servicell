from django.forms import ModelForm

from .models import Inversion

class InversionForm(ModelForm):
    class Meta:
        model = Inversion
        fields = '__all__'