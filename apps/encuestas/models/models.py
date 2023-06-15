from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True, blank=True, null=True)
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


class TipoMomento(BaseModel):
    tipo = models.CharField(max_length=256)

    class Meta:
        verbose_name = "TipoMomento"
        verbose_name_plural = "TipoMomentos"


class Question(BaseModel):
    pregunta_nombre = models.CharField(max_length=500)
    momento = models.ForeignKey(TipoMomento, on_delete=models.CASCADE, db_index=True)
    tipo_pregunta = models.CharField(max_length=100, blank=True, null=True)
    depende_respuesta = models.ForeignKey(
        "Answer", on_delete=models.CASCADE, blank=True, null=True
    )
    componente = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Question"


class Answer(BaseModel):
    respuesta = models.CharField(max_length=256)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    pregunta = models.ForeignKey(Question, on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = "Answers"
        verbose_name_plural = "Answers"
