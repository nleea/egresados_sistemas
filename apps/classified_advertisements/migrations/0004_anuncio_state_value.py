# Generated by Django 4.1.2 on 2023-08-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0003_remove_anuncio_mensajes_anuncio_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='state_value',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]
