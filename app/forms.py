from django import forms
from .models import Aspirante
from .models import *

class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','name']



class AspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ["nombre","correo","nombre_invocador","servidor","Liga"]
