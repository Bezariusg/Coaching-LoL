from django import forms
<<<<<<< HEAD
from .models import *
class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','name']
=======
from .models import Aspirante

class AspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ["nombre","correo","nombre_invocador","servidor","Liga"]
>>>>>>> d2a67ff9ddc6f4ead98d2c5d58038a9fb89fa0c0
