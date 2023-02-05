from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    name = models.CharField(max_length=256,blank=True,null=True)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
<<<<<<< HEAD
    userCreate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    userUpdate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
=======
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
    
    class Meta:
        abstract = True


class Seccion(BaseModel):
    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural = 'Seccions'


class Categoria(BaseModel):
    seccionId = models.ForeignKey(Seccion,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(BaseModel):
    categoriId = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'


class Anuncio(BaseModel):
    datos = models.CharField(max_length=256)
<<<<<<< HEAD
    persona_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    subCategori = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)

=======
    persona_id = models.ForeignKey(User,on_delete=models.CASCADE)
    subCategori = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'