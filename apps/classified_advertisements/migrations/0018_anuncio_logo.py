# Generated by Django 4.1.2 on 2023-05-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_advertisements', '0017_alter_anuncio_visible_alter_categoria_visible_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='static/files/advertisements/'),
        ),
    ]