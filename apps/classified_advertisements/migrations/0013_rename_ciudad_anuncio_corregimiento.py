# Generated by Django 4.1.2 on 2023-04-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0012_rename_descripción_anuncio_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='ciudad',
            new_name='corregimiento',
        ),
    ]
