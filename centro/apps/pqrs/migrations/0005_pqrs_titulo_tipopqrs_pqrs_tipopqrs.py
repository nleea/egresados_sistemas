# Generated by Django 4.1.2 on 2023-02-14 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pqrs', '0004_alter_asignacion_fecha_asignacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqrs',
            name='titulo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='TipoPqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('tipo', models.CharField(max_length=256)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pqrs',
            name='tipopqrs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pqrs.tipopqrs'),
        ),
    ]
