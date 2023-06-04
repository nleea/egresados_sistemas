# Generated by Django 4.1.2 on 2023-06-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0011_alter_persons_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='identification',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='persons',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
