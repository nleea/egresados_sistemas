# Generated by Django 4.1.2 on 2023-05-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0004_alter_resources_roles_alter_resources_roles_rolesid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_types',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faculties',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='genders',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='headquarters',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='programs',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='resources',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='resources_roles',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user_roles',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
