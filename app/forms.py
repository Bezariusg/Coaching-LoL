from django import forms
from .models import Aspirante

class AspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ["nombre","correo","nombre_invocador","servidor","Liga"]
