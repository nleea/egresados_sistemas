# Generated by Django 4.1.2 on 2023-06-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_answer_visible_question_visible_tipomomento_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tipo_pregunta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]