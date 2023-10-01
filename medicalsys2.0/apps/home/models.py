from django.db import models

# Create your models here.

class especialidades (models.Model):
    title = models.CharField(max_length=200,verbose_name= "Titulo") #cadena de caracteres, dentro del parantesis ponemos cuantos caracteres permite/traducimos el nombre
    description = models.TextField (verbose_name="Descripcion") #cadena de texto
    image = models.ImageField(verbose_name= "Imagen",upload_to= "projects") # campo de imagen, el upload to crea en la carpeta media un directorio de los proyectos ahi adentro
    #almacenara fecha de creacion y de actualizacion
    created = models.DateTimeField(auto_now_add=True,verbose_name= "Fecha de creacion") #fecha y hora/graba la hora en la primera hora crerada
    updated = models.DateTimeField (auto_now=True,verbose_name= "Fecha de edicion") 

#traduciremos el nombre del proyecto en este caso Project, ya que dentro de la app nos aparecia en EN y lo queremos en ES

    class Meta :
        verbose_name = "especialiadad"
        verbose_name_plural = "especialidades"
        ordering =["-created"] #ordenamos el orden en cual cargamos un proyecto, del mas nuevo al mas viejo

    def __str__ (self): #asignamos el titulo del proyecto cargado
        return self.title