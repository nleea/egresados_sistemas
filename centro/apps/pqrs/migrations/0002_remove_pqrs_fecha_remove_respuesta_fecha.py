# Generated by Django 4.1.2 on 2023-02-08 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pqrs',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='fecha',
        ),
    ]
