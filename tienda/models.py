from django.db import models

# Create your models here.
#identificar los elementos de la tabla
class Hoja(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    imagen=models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    #se crea la carpeta imagenes ya que no esta.
    descripcion=models.TextField(verbose_name='Descripción', null=True)

#para mostrar la fila
    def __str__(self):
        fila="Nombre:"+self.nombre+"-"+"Descripción:"+self.descripcion
        return fila

#para borrar la imagen por completo-es decir la que esta en la carpeta imagenes
    def delete(self,using=None, kepp_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()