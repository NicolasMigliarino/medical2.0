from django.contrib import admin
from .models import especialidades

# Register your models here.




#creamos la clase para ver dentro del admin la fecha de creacion y edicion pero solo para lectura
class ProjectAdmin (admin.ModelAdmin): #creamos una clase hereda de model.admin
    readonly_fields = ('created','updated')   #una tupla o lista solo de lectura

admin.site.register(especialidades,ProjectAdmin)
