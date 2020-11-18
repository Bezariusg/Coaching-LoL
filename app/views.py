from django.shortcuts import render
<<<<<<< HEAD
from .models import *
from django.forms import modelformset_factory

=======
from .forms import AspiranteForm
from django.contrib import messages
>>>>>>> d2a67ff9ddc6f4ead98d2c5d58038a9fb89fa0c0

# Create your views here.

def home(request):
    return render (request, 'app/home.html')

<<<<<<< HEAD

=======
>>>>>>> d2a67ff9ddc6f4ead98d2c5d58038a9fb89fa0c0
def galeria(request):
    return render (request, 'app/galeria.html')


def quienes_somos(request):
    return render (request, 'app/quienes_somos.html')


def registrate(request):
<<<<<<< HEAD
    return render (request, 'app/registrate.html')

def image_gallery(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'app/image_gallery.html', {'images': images})
=======
    data = {
        'form': AspiranteForm()
    }

    if request.method == 'POST':
        formulario = AspiranteForm(data=request.POST)
        if formulario.is_valid():

            formulario.save()
            messages.success(request, 'Registro Exitoso')

        else:
            data["form"] = formulario


    return render (request, 'app/registrate.html',data)
>>>>>>> d2a67ff9ddc6f4ead98d2c5d58038a9fb89fa0c0
