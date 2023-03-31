from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+")
    userUpdate = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+")

    class Meta:
        abstract = True


class Eventos(BaseModel):
    area = models.CharField(max_length=256)
    subArea = models.CharField(max_length=256)
    nombre_actividad = models.CharField(max_length=256)
    tipo_actividad = models.CharField(max_length=256)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    lugar = models.CharField(max_length=256)
    cupos = models.IntegerField()
    descripcion = models.CharField(max_length=600)
    objectivo = models.CharField(max_length=600)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
