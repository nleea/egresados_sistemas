# Generated by Django 4.1.2 on 2023-08-14 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0035_alter_inscripcion_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 8, 14)),
        ),
    ]
