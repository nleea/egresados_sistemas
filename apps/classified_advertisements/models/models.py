from django.db import models
from django.contrib.auth import get_user_model
from .managers import SubCategoryManagers, AdvertisementsManagers

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


class Categoria(BaseModel):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(BaseModel):
    categoriId = models.ForeignKey(
        Categoria, related_name="_id", on_delete=models.CASCADE, blank=True, null=True)

    objects = SubCategoryManagers()

    class Meta:
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'


class TiposCapacitaciones(BaseModel):
    class Meta:
        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitacitaciones'


class Anuncio(BaseModel):

    nombre_emprendimiento = models.CharField(
        max_length=256, null=False, blank=False)
    descripción = models.CharField(max_length=300, blank=False, null=False)
    telefono_emprendimiento = models.CharField(
        max_length=11, blank=False, null=False)
    correo_emprendimiento = models.EmailField(null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    municipio = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    subCategori = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    metodos_entrega = models.CharField(max_length=300)
    formas_pago = models.CharField(max_length=300)
    tipo_capacitacion = models.ForeignKey(
        TiposCapacitaciones, on_delete=models.CASCADE)

    objects = AdvertisementsManagers()

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'


class RedesSociales(BaseModel):
    link = models.CharField(max_length=500, blank=False, null=False)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)


class AnuncioHasRedes(BaseModel):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    redes = models.ForeignKey(RedesSociales, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=500)


class Producto(BaseModel):
    precio = models.CharField(max_length=256)
    cantidad = models.CharField(max_length=256)
