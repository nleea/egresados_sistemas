# Generated by Django 4.1.2 on 2023-04-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0002_faculties_headquarters_programs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculties',
            name='name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headquarters',
            name='name',
            field=models.CharField(default='riohacha', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programs',
            name='name',
            field=models.CharField(default='rio', max_length=256),
            preserve_default=False,
        ),
    ]
