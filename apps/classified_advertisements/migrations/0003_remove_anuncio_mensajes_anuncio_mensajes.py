# Generated by Django 4.1.2 on 2023-08-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0002_anuncio_state_mensajes_anuncio_mensajes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='mensajes',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='mensajes',
            field=models.ManyToManyField(null=True, to='classified_advertisements.mensajes'),
        ),
    ]
