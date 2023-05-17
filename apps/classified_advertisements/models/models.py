from django.db import models
from django.contrib.auth import get_user_model
from .managers import SubCategoryManagers, AdvertisementsManagers

User = get_user_model()


class BaseModel(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+",db_index=True)
    userUpdate = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+",db_index=True)
    visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categoria(BaseModel):

    def __str__(self) -> str:
        return self.name  # type:ignore

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(BaseModel):
    categoriaId = models.ForeignKey(
        Categoria, related_name="_id", on_delete=models.CASCADE, blank=True, null=True,db_index=True)

    objects = SubCategoryManagers()
    
    
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'


class TiposCapacitaciones(BaseModel):
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitacitaciones'

class RedesSociales(BaseModel):
    link = models.CharField(max_length=500, blank=False, null=False)

class Anuncio(BaseModel):

    nombre_emprendimiento = models.CharField(
        max_length=256, null=False, blank=False)
    descripcion = models.CharField(max_length=300, blank=False, null=False)
    telefono_emprendimiento = models.CharField(
        max_length=11, blank=False, null=False)
    correo_emprendimiento = models.EmailField(null=False, blank=False)
    corregimiento = models.CharField(max_length=50, null=False, blank=False)
    municipio = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    subCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE,db_index=True)
    metodos_entrega = models.CharField(max_length=300)
    formas_pago = models.CharField(max_length=300)
    tipo_capacitacion = models.ManyToManyField(
        TiposCapacitaciones,db_index=True)
    redes = models.ManyToManyField(RedesSociales,related_name="redes_store",db_index=True)

    objects = AdvertisementsManagers()

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'


class Producto(BaseModel):
    precio = models.CharField(max_length=256)
    cantidad = models.CharField(max_length=256)
