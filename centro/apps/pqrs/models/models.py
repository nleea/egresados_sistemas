from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True,blank=True, null=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    userUpdate = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    
    class Meta:
        abstract = True

class Pqrs(BaseModel):
    description = models.CharField(max_length=256)
    persona = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pqrs'

class Asignacion(BaseModel):
    funcionarioId = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now=True)
    pqrs = models.ForeignKey(Pqrs,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Asignacion'
        verbose_name_plural = 'Asignacions'

class Anexo(BaseModel):
    nombre_ane =models.CharField(max_length=256)
    
    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'

class Respuesta(BaseModel):
    pqrs = models.ForeignKey(Pqrs,on_delete=models.CASCADE,related_name="respuesta_pqrs")
    anexo = models.ForeignKey(Anexo,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
