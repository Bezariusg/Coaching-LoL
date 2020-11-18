from django.shortcuts import render
from .models import *
from django.forms import modelformset_factory


# Create your views here.

def home(request):
    return render (request, 'app/home.html')


def galeria(request):
    return render (request, 'app/galeria.html')


def quienes_somos(request):
    return render (request, 'app/quienes_somos.html')


def registrate(request):
    return render (request, 'app/registrate.html')

def image_gallery(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'app/image_gallery.html', {'images': images})
