# Generated by Django 4.1.2 on 2023-06-15 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0025_alter_eventos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 6, 15)),
        ),
    ]