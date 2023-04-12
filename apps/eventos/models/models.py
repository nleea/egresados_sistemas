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


class EventosArea(BaseModel):
    class Meta:
        verbose_name = "Area Evento"
        verbose_name_plural = "Areas Eventos"


class SubAreaEventos(BaseModel):
    area = models.ForeignKey(
        EventosArea, on_delete=models.CASCADE, related_name="areas")

    class Meta:
        verbose_name = "Sub Area Evento"
        verbose_name_plural = "Sub Areas Eventos"


class Eventos(BaseModel):
    area = models.ForeignKey(
        EventosArea, on_delete=models.CASCADE, related_name="+")
    subArea = models.ForeignKey(
        SubAreaEventos, on_delete=models.CASCADE, related_name="+")
    nombre_actividad = models.CharField(max_length=256)
    tipo_actividad = models.CharField(max_length=256)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    hora = models.CharField(max_length=10)
    lugar = models.CharField(max_length=256)
    cupos = models.IntegerField()
    descripcion = models.CharField(max_length=600)
    objectivo = models.CharField(max_length=600)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
