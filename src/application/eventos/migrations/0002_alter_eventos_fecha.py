# Generated by Django 4.1.2 on 2023-12-27 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 12, 27)),
        ),
    ]
