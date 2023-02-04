from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TipoMomento(models.Model):
    tipo = models.CharField(max_length=256)
    
    class Meta:
        verbose_name = "TipoMomento"
        verbose_name_plural = "TipoMomentos"
        
class Pregunta(models.Model):
    pregunta_nombre = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_created=True)
    momento = models.ForeignKey(TipoMomento,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"


class Respuesta(models.Model):
    respuesta = models.CharField(max_length=256)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)