# Generated by Django 4.1.2 on 2024-02-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0003_alter_anuncio_createdat_alter_categoria_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='corregimiento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='municipio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
