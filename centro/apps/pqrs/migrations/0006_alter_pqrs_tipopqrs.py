# Generated by Django 4.1.2 on 2023-02-15 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0005_pqrs_titulo_tipopqrs_pqrs_tipopqrs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='tipopqrs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pqrs.tipopqrs'),
            preserve_default=False,
        ),
    ]
