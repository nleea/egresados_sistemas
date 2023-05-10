from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Pqrs,Asignacion

@receiver(post_save, sender=Asignacion)
def crear_usuario_artista(sender, instance, created, **kwargs):
    if created:
        obj = Pqrs.objects.get(id=instance.pqrs.id)
        obj.status = "EP"
        obj.save()