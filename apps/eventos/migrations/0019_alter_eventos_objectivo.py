# Generated by Django 4.1.2 on 2023-05-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0018_alter_eventos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='objectivo',
            field=models.CharField(max_length=300),
        ),
    ]
