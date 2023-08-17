from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date
from apps.auth_module.models import Programs
from configs.helpers.hour import readeable_hour
import datetime

User = get_user_model()


class BaseModel(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        db_index=True,
    )
    userUpdate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        db_index=True,
    )
    visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class EventosArea(BaseModel):
    def __str__(self) -> str:
        return self.name  # type: ignore

    class Meta:
        verbose_name = "Area Evento"
        verbose_name_plural = "Areas Eventos"


class SubAreaEventos(BaseModel):
    area = models.ForeignKey(
        EventosArea, on_delete=models.CASCADE, related_name="areas", db_index=True
    )

    class Meta:
        verbose_name = "Sub Area Evento"
        verbose_name_plural = "Sub Areas Eventos"


class TipoEvento(BaseModel):
    class Meta:
        verbose_name = "Tipo Evento"
        verbose_name_plural = "Tipo Eventos"


class Eventos(BaseModel):
    area = models.ForeignKey(
        EventosArea, on_delete=models.CASCADE, related_name="+", db_index=True
    )
    subArea = models.ForeignKey(
        SubAreaEventos, on_delete=models.CASCADE, related_name="+", db_index=True
    )
    nombre_actividad = models.CharField(max_length=256)
    tipo_actividad = models.CharField(max_length=256)
    responsable = models.CharField(max_length=256)
    tipo = models.ForeignKey(
        TipoEvento, on_delete=models.CASCADE, blank=True, null=True, db_index=True
    )
    fecha = models.DateField(blank=False, null=False, default=timezone.now().date())
    hora = models.CharField(max_length=10)
    lugar = models.CharField(max_length=256)
    cupos = models.IntegerField()
    descripcion = models.CharField(max_length=600)
    objectivo = models.CharField(max_length=300)
    dirigido = models.ForeignKey(Programs, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.fecha < date.today() or readeable_hour(
            self.hora
        ) < datetime.datetime.now().strftime("%H:%M"):
            raise Exception("No se puede crear un evento para una fecha pasada")
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class Inscripcion(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        unique_together = ("evento", "user")


class Asistencia(BaseModel):
    evento = models.ForeignKey(
        Eventos, on_delete=models.CASCADE, db_index=True, unique=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="+", unique=False
    )
    confirm = models.BooleanField(default=False)
    asistencia = models.BooleanField(default=False)

    def clean(self):
        if self.evento.fecha < date.today():
            raise ValidationError(
                "No se puede crear la asistencia para un evento que ha pasado."
            )

    class Meta:
        unique_together = ("evento", "user")
