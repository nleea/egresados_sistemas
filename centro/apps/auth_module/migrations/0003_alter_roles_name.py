# Generated by Django 4.1.2 on 2022-11-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0002_alter_user_roles_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
