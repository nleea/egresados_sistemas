# Generated by Django 4.1.2 on 2023-02-04 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from configs.helpers.menu_resources import menuResources
from configs.helpers.menu import resources as menu_resources
import re
from django.contrib.auth.hashers import make_password


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    def insert_init_data(apps, schema_editor):
        User = apps.get_model("auth_module", "User")
        User.objects.bulk_create(
            [
                User(
                    username="admin",
                    email="admin@gmail.com",
                    password=make_password("12345678"),
                    is_staff=True,
                ),
                User(
                    username="egresado",
                    email="egresado@gmail.com",
                    password=make_password("12345678"),
                ),
            ]
        )

        Roles = apps.get_model("auth_module", "groups")
        Roles.objects.bulk_create(
            [Roles(name="Admin"), Roles(name="Egresado"), Roles(name="General")]
        )
        

        User_roles = apps.get_model("auth_module", "User_roles")
        user = User.objects.all()
        roles = Roles.objects.all()
        list_user_roles = []
        for u in user:
            for r in roles:
                if u.username == "egresado" and r.name == "Admin":
                    continue
                list_user_roles.append(
                    User_roles(userId=u, rolesId=r),
                )
        User_roles.objects.bulk_create(list_user_roles)

        Resources = apps.get_model("auth_module", "Resources")  # type: ignore
        resources = []
        menuResources(menu_resources, resources, Resources, 1)
        resources = Resources.objects.bulk_create(resources)

        Resources_roles = apps.get_model("auth_module", "Resources_roles")  # type: ignore
        list_resources_roles = []
        rol = Roles.objects.all()

        for rl in rol:
            for r in resources:
                if rl.name != "Admin" and re.search("admin", r.link) is not None:
                    continue
                else:
                    list_resources_roles.append(
                        Resources_roles(rolesId=rl, resourcesId=r)
                    )

        Resources_roles.objects.bulk_create(list_resources_roles)

    def undo_insert_data(apps, schema_editor):
        User_roles = apps.get_model("auth_module", "User_roles")
        User_roles.objects.all().delete()
        Roles = apps.get_model("auth_module", "Roles")
        Roles.objects.all().delete()
        User = apps.get_model("auth_module", "User")
        User.objects.all().delete()
        Resources_roles = apps.get_model("auth_module", "Resources_roles")
        Resources_roles.objects.all().delete()
        Resources = apps.get_model("auth_module", "Resources")
        Resources.objects.all().delete()

    operations = [
        migrations.CreateModel(
            name="Anexo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_ane", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Anexo",
                "verbose_name_plural": "Anexos",
            },
        ),
        migrations.CreateModel(
            name="Pqrs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField(auto_created=True)),
                ("description", models.CharField(max_length=256)),
                (
                    "persona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Pqrs",
            },
        ),
        migrations.CreateModel(
            name="Respuesta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateTimeField(auto_now=True)),
                (
                    "anexo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pqrs.anexo"
                    ),
                ),
                (
                    "pqrs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respuesta_pqrs",
                        to="pqrs.pqrs",
                    ),
                ),
            ],
            options={
                "verbose_name": "Respuesta",
                "verbose_name_plural": "Respuestas",
            },
        ),
        migrations.CreateModel(
            name="Asignacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_asignacion", models.DateField(auto_created=True)),
                (
                    "funcionarioId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pqrs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pqrs.pqrs"
                    ),
                ),
            ],
            options={
                "verbose_name": "Asignacion",
                "verbose_name_plural": "Asignacions",
            },
        ),
        # migrations.RunPython(
        #     insert_init_data, reverse_code=undo_insert_data, atomic=True
        # ),
    ]
