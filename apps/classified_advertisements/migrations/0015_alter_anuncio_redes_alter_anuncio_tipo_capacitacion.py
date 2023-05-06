# Generated by Django 4.1.2 on 2023-04-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0014_rename_categoriid_subcategoria_categoriaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='redes',
            field=models.ManyToManyField(db_index=True, related_name='redes_store', to='classified_advertisements.redessociales'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='tipo_capacitacion',
            field=models.ManyToManyField(db_index=True, to='classified_advertisements.tiposcapacitaciones'),
        ),
    ]