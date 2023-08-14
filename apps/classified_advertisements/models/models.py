from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from .managers import SubCategoryManagers, AdvertisementsManagers
from apps.validators.index import validate_image, extension_type

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


class Categoria(BaseModel):
    def __str__(self) -> str:
        return self.name  # type:ignore

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class SubCategoria(BaseModel):
    categoriaId = models.ForeignKey(
        Categoria,
        related_name="_id",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )

    objects = SubCategoryManagers()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubCategoria"
        verbose_name_plural = "SubCategorias"


class TiposCapacitaciones(BaseModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Capacitacion"
        verbose_name_plural = "Capacitacitaciones"


class RedesSociales(BaseModel):
    link = models.CharField(max_length=500, blank=False, null=False)


class Mensajes(BaseModel):
    mensaje = models.CharField(max_length=500, default="")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"


class Anuncio(BaseModel):
    nombre_emprendimiento = models.CharField(max_length=256, null=False)
    descripcion = models.CharField(max_length=600, null=False)
    telefono_emprendimiento = models.CharField(max_length=11, null=False)
    correo_emprendimiento = models.EmailField(null=False)
    corregimiento = models.CharField(max_length=50, null=False)
    municipio = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    subCategoria = models.ForeignKey(
        SubCategoria, on_delete=models.CASCADE, db_index=True
    )
    metodos_entrega = models.CharField(max_length=900)
    formas_pago = models.CharField(max_length=900)
    tipo_capacitacion = models.ManyToManyField(TiposCapacitaciones, db_index=True)
    redes = models.ManyToManyField(
        RedesSociales, related_name="redes_store", db_index=True
    )
    logo = models.FileField(
        upload_to="eventos/%Y/",
        blank=True,
        null=True,
        validators=[validate_image, extension_type],
    )
    state = models.BooleanField(default=False)
    state_value = models.CharField(max_length=50,default="Pendiente")
    mensajes = models.ManyToManyField(Mensajes, null=True)

    objects = AdvertisementsManagers()

    def change_state(self, state):
        self.state = state
        self.state_value = "Verificado" if state else "Pendiente"
        self.save()

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"


class VotoAnuncio(models.Model):
    emprendimiento = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("emprendimiento", "user")
