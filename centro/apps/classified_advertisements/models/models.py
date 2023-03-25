from django.db import models
from django.contrib.auth import get_user_model
from .managers import SubCategoryManagers

User = get_user_model()

class BaseModel(models.Model):
    name = models.CharField(max_length=256,blank=True,null=True)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    userUpdate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    
    class Meta:
        abstract = True


class Categoria(BaseModel):

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(BaseModel):
    categoriId = models.ForeignKey(Categoria,related_name="_id",on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta:
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'

class RedesSociales(BaseModel):
    link = models.CharField(max_length=500,blank=False,null=False)
    

class TiposCapacitaciones(BaseModel):
    tipo = models.CharField(max_length=50)


class Anuncio(BaseModel):
    
    METHOD_ASSETS = [
        ("1","Domicilio"),
        ("2","Recogido en la tienda"),
        ("3","Envio por correo"),
        ("4","Domicilio y Recogido en la tienda"),
        ("5","Recogido en la tienda y Envio por correo")
    ]
    
    METHOD_PAYMENTS = [
        ("1","Tranferencia"),
        ("2","Efectivo"),
        ("3","Contra Entrega"),
        ("4","Tranferencia y Efectivo"),
        ("5","Tranferencia y Contra Entrega")
    ]

    OPTIONS = [
        ("si","SI"),
        ("no","NO")
    ]

    nombre_emprendimiento = models.CharField(max_length=256,null=False,blank=False)
    descripción = models.CharField(max_length=300,blank=False,null=False)
    telefono_emprendimiento = models.CharField(max_length=11,blank=False,null=False)
    correo_emprendimiento = models.EmailField(null=False,blank=False)
    ciudad = models.CharField(max_length=50,null=False,blank=False)
    municipio = models.CharField(max_length=50,null=False,blank=False)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    persona_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    subCategori = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    redes = models.ManyToManyField(RedesSociales,through="AnuncioHasRedes")
    entrega_cuentas = models.CharField(max_length=30,choices=METHOD_ASSETS)
    formas_pago = models.CharField(max_length=30,choices=METHOD_PAYMENTS)
    capacitacion = models.CharField(max_length=20,choices=OPTIONS)
    tipo_capacitacion = models.ForeignKey(TiposCapacitaciones,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'


class AnuncioHasRedes(BaseModel):
    anuncio = models.ForeignKey(Anuncio,on_delete=models.CASCADE)
    redes = models.ForeignKey(RedesSociales,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=500)


