from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from src.validators.index import validate_image, extension_type
from src.application.default.models import BaseModel

User = get_user_model()


class TipoPqrs(BaseModel):
    tipo = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.tipo


class Pqrs(BaseModel):
    class STATUS_PQRS(models.TextChoices):
        FINALIZADA = "FN", _("Finalizada")
        ACTIVA = "AC", _("Activa")
        ESPERA = "EP", _("En espera")

    titulo = models.CharField(max_length=256)
    description = models.CharField(max_length=600)
    persona = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    tipopqrs = models.ForeignKey(TipoPqrs, on_delete=models.CASCADE, db_index=True)
    anexo = models.FileField(
        upload_to="pqrs/%Y/",
        blank=True,
        null=True,
        validators=[validate_image, extension_type],
    )
    status = models.CharField(
        choices=STATUS_PQRS.choices, max_length=10, default=STATUS_PQRS.ACTIVA
    )

    class Meta:
        verbose_name = "Pqrs"

    def __str__(self):
        return self.titulo


class Asignacion(BaseModel):
    funcionarioId = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    fecha_asignacion = models.DateField(auto_now=True)
    pqrs = models.ForeignKey(Pqrs, on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignacions"


class Respuesta(BaseModel):
    pqrs = models.ForeignKey(
        Pqrs, on_delete=models.CASCADE, related_name="respuesta_pqrs", db_index=True
    )
    anexo = models.FileField(upload_to="pqrs/%Y/respuesta/", blank=True, null=True)
    descripcion = models.CharField(max_length=600, null=True, blank=True)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
