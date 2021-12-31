from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import User
# Create your models here.

def upload_path(instance,filename):
    return '/'.join('archivos',str(instance.nombre),filename)

class Carpetas(TimeStampedModel):
    nombre = models.CharField('Titulo',max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)+ '-' +self.nombre


class Archivos(TimeStampedModel):
    carpeta = models.ForeignKey(Carpetas,on_delete=models.CASCADE)
    archivo=models.FileField('Archivos',upload_to='archivos')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_nombre_archivo(self):
        nombre = str(self.archivo).split("/")
        return nombre
