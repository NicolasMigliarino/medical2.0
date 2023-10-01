from django.shortcuts import render
from .models import especialidades


# Create your views here.
from django.views.generic import TemplateView,ListView

class IndexView (TemplateView):
    template_name='home/home.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!

class InfoView (TemplateView):
    template_name='home/info.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!


class especialiadadListView(ListView):
    template_name='home/especialidades.html' # ruta donde se cuentra el template ¡Recordar que se ubica en la carpeta template a la altura del manage.py!
    context_object_name = 'projects' # su propio nombre para la lista como variable de plantilla
    def get_queryset(self):
        return especialidades.objects.all()

