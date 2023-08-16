# Generated by Django 4.1.2 on 2023-08-12 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0033_alter_asistencia_asistencia_alter_asistencia_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='user',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]