# Generated by Django 4.1.2 on 2023-08-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0012_alter_persons_identification_alter_persons_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_module.programs'),
        ),
    ]