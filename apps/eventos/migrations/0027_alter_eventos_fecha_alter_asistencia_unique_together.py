# Generated by Django 4.1.2 on 2023-06-21 21:30

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0026_alter_eventos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 6, 21)),
        ),
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together={('evento', 'user')},
        ),
    ]