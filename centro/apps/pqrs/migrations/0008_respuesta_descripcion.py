# Generated by Django 4.1.2 on 2023-02-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0007_alter_pqrs_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
