# Generated by Django 4.1.2 on 2024-02-06 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0005_alter_persons_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2024, 2, 6)),
        ),
    ]
