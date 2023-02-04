from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()




class Pqrs(models.Model):
    description = models.CharField(max_length=256)
    fecha = models.DateTimeField(auto_created=True)
    persona = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pqrs'

class Asignacion(models.Model):
    funcionarioId = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_created=True)
    pqrs = models.ForeignKey(Pqrs,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Asignacion'
        verbose_name_plural = 'Asignacions'

class Anexo(models.Model):
    nombre_ane =models.CharField(max_length=256)
    
    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'

class Respuesta(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    pqrs = models.ForeignKey(Pqrs,on_delete=models.CASCADE,related_name="respuesta_pqrs")
    anexo = models.ForeignKey(Anexo,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
