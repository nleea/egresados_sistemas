# Generated by Django 4.1.2 on 2023-05-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0018_anuncio_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.CharField(max_length=600),
        ),
    ]
