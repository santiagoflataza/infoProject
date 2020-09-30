from django import forms
from .models import Rubro

class RubroCrear(forms.ModelForm):

    class Meta:
        model = Rubro
        fields = [nombre]
