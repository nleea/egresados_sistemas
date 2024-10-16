# Generated by Django 4.1.2 on 2023-12-23 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from configs.helpers.menu_resources import menuResources
from configs.helpers.menu import resources as menu_resources, resources_egresado
import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    def insert_init_data(apps, schema_editor):
        
        TipoPqrs = apps.get_model("pqrs", "TipoPqrs")
        TipoPqrs.objects.bulk_create(
            [
                TipoPqrs(tipo="PETICIONES"), 
                TipoPqrs(tipo="QUEJAS"), 
                TipoPqrs(tipo="RECLAMOS"), 
                TipoPqrs(tipo="SUGERENCIAS"), 
            ]
        )
        
        Headquarters = apps.get_model("auth_module", "Headquarters")
        Faculties = apps.get_model("auth_module", "Faculties")
        Programs = apps.get_model("auth_module", "Programs")
        
        Headquarters.objects.bulk_create(
            [
                Headquarters(name="SEDE RIOHACHA"), 
                Headquarters(name="SEDE MAICAO"),
                Headquarters(name="SEDE FONSECA"),
            ]
        )
             
        Faculties.objects.bulk_create(
            [
                Faculties(name="FACULTAD DE INGENIERIA", headquarter_id=1), 
                Faculties(name="FACULTAD DE LA SALUD", headquarter_id=2), 
                Faculties(name="FACULTAD DE CIENCIAS BASICAS", headquarter_id=3), 
            ]
        )
             
        Programs.objects.bulk_create(
            [
                Programs(name="PROGRAMA DE INGENIERIA DE SISTEMAS", faculty_id=1), 
                Programs(name="PROGRAMA DE INGENIERIA CIVIL", faculty_id=1), 
                Programs(name="PROGRAMA DE INGENIERIA ELECTRICA", faculty_id=1), 
                Programs(name="PROGRAMA DE INGENIERIA INDUSTRIAL", faculty_id=1), 
                Programs(name="PROGRAMA DE NUTRICION", faculty_id=2), 
                Programs(name="PROGRAMA DE ENFERMERIA", faculty_id=2), 
                Programs(name="PROGRAMA DE BIOLOGIA", faculty_id=3), 
                Programs(name="PROGRAMA DE AGROECOLOGIA", faculty_id=3), 
            ]
        )
             

        EventosArea = apps.get_model("eventos", "EventosArea")
        SubAreaEventos = apps.get_model("eventos", "SubAreaEventos")
        TipoEvento = apps.get_model("eventos", "TipoEvento")
        
        EventosArea.objects.bulk_create(
            [
                EventosArea(name="BOLSA DE EMPLEO"), 
                EventosArea(name="APOYO AL GRADUADO"),
                EventosArea(name="INVESTIGACIONES"), 
                EventosArea(name="RECURSOS HUMANOS"),
            ]
        )
        SubAreaEventos.objects.bulk_create(
            [
                SubAreaEventos(name="FERIA DE EMPLEO", area_id=1), 
                SubAreaEventos(name="CARNETIZACIÓN", area_id=2),
                SubAreaEventos(name="GESTION DE PROYECTOS", area_id=3), 
                SubAreaEventos(name="SOLUCION DE CONFLICTOS", area_id=4),
            ]
        )
        TipoEvento.objects.bulk_create(
            [
                TipoEvento(name="TALLERES"), 
                TipoEvento(name="CONFERENCIAS"),
                TipoEvento(name="FOROS"), 
                TipoEvento(name="ESPACIO RADIAL"),
            ]
        )
        
        TipoMomento = apps.get_model("encuestas", "TipoMomento")
        TipoMomento.objects.bulk_create(
            [
                TipoMomento(tipo="PRIMER AÑO"), 
                TipoMomento(tipo="SEGUNDO AÑO"),
                TipoMomento(tipo="TERCER AÑO"), 
                TipoMomento(tipo="CUARTO AÑO"),
            ]
        )
        
        Categoria = apps.get_model("classified_advertisements", "Categoria")
        SubCategoria = apps.get_model("classified_advertisements", "SubCategoria")
        TiposCapacitaciones = apps.get_model("classified_advertisements", "TiposCapacitaciones")
        
        TiposCapacitaciones.objects.bulk_create(
            [
                TiposCapacitaciones(name="MARKETING DIGITAL"), 
                TiposCapacitaciones(name="GESTION FINANCIERA"),
                TiposCapacitaciones(name="GESTION DE TIEMPO Y PRODUCTIVIDAD"), 
                TiposCapacitaciones(name="DESARROLLO DE LIDERAZGO"),
            ]
        )
        Categoria.objects.bulk_create(
            [
                Categoria(name="SALUD Y BIENESTAR"), 
                Categoria(name="COMERCIO Y VENTAS"),
                Categoria(name="TECNOLOGIA Y DESARROLLO"), 
                Categoria(name="ARTE Y DISEÑO"),
            ]
        )
        SubCategoria.objects.bulk_create(
            [
                SubCategoria(name="Fitness y entrenamiento personal", categoriaId_id=1), 
                SubCategoria(name="Nutrición", categoriaId_id=1), 
                SubCategoria(name="Tiendas en línea", categoriaId_id=2),
                SubCategoria(name="Franquicias", categoriaId_id=2),
                SubCategoria(name="Comercio electrónico", categoriaId_id=3), 
                SubCategoria(name="Diseño de interiores", categoriaId_id=4),
                SubCategoria(name="AProducción audiovisual", categoriaId_id=4),
            ]
        )
        
        
        User = apps.get_model("auth_module", "User")
        Person = apps.get_model("auth_module", "Persons")
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
                User(
                    username="usuarioanonimo@uniguajira.edu.co",
                    email="usuarioanonimo@uniguajira.edu.co",
                    password=make_password("2023082386"),
                ),
            ]
        )

        Group.objects.bulk_create(
            [Group(name="Admin"), Group(name="Egresado"), Group(name="General"), Group(name="Invitado Anonimo")]
        )

        User_roles = apps.get_model("auth_module", "user_groups")
        User_documents = apps.get_model("auth_module", "document_types")
        User_genders = apps.get_model("auth_module", "genders")

        User_documents.objects.bulk_create(
            [User_documents(name="CEDULA DE CIUDADANIA"), User_documents(name="DOCUMENTO DE IDENTIDAD"), User_documents(name="PASAPORTE")]
        )

        User_genders.objects.bulk_create(
            [User_genders(name="MASCULINO"), User_genders(name="FEMENINO"), User_genders(name="OTRO")]
        )

        Person.objects.bulk_create(
            [
                Person(
                    name="Nelson",
                    surname="De castro",
                    identification="11188725845",
                    address="Cll 15# 21-89",
                    document_type_id=1,
                    gender_type_id=1,
                    user_id=1,
                    phone="000000000",
                ),
                Person(
                    name="Oscar",
                    surname="Arregoces",
                    identification="11188725946",
                    address="Cll 15# 21-89",
                    document_type_id=1,
                    gender_type_id=1,
                    user_id=2,
                    phone="000000000",
                ),
                Person(
                    name="Invitado",
                    surname="Anonimo",
                    identification="111111111",
                    address="Cll 24# 21-89",
                    document_type_id=1,
                    gender_type_id=1,
                    user_id=3,
                    phone="3020102331",
                ),
            ]
        )

        user = User.objects.all()
        roles = Group.objects.all()
        list_user_roles = []
        for u in user:
            for r in roles:
                if u.username == "egresado" and r.name == "Egresado":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id),
                    )
                elif u.username == "admin" and r.name == "Admin":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id),
                    )
                elif u.username == "usuarioanonimo@uniguajira.edu.co" and r.name == "Invitado Anonimo":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id),
                    )

        User_roles.objects.bulk_create(list_user_roles)

        Resources = apps.get_model("auth_module", "Resources")  # type: ignore
        resources = []
        resources_egresado_bulk = []
        menuResources(menu_resources, resources, Resources, 1)
        menuResources(
            resources_egresado, resources_egresado_bulk, Resources, len(resources) + 1
        )
        resources = Resources.objects.bulk_create(resources)
        resources_egresado_bulk = Resources.objects.bulk_create(resources_egresado_bulk)

        Resources_roles = apps.get_model("auth_module", "Resources_roles")  # type: ignore
        list_resources_roles = []
        rol = Group.objects.all()

        for rl in rol:
            if rl.name == "Egresado" or rl.name == "General":
                for r in resources_egresado_bulk:
                    list_resources_roles.append(
                        Resources_roles(rolesId_id=rl.id, resourcesId=r)
                    )
            if rl.name == "Admin" or rl.name == "Invitado Anonimo":
                for r in resources:
                    list_resources_roles.append(
                        Resources_roles(rolesId_id=rl.id, resourcesId=r)
                    )

        Resources_roles.objects.bulk_create(list_resources_roles)

    def undo_insert_data(apps, schema_editor):
        User_roles = apps.get_model("auth_module", "User_roles")
        User_roles.objects.all().delete()
        # Roles = apps.get_model("auth_module", "Roles")
        Group.objects.all().delete()
        User = apps.get_model("auth_module", "User")
        User.objects.all().delete()
        Resources_roles = apps.get_model("auth_module", "Resources_roles")
        Resources_roles.objects.all().delete()
        Resources = apps.get_model("auth_module", "Resources")
        Resources.objects.all().delete()

    operations = [
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
                ("createdAt", models.DateField(auto_now_add=True, null=True)),
                ("updateAt", models.DateField(auto_now=True, null=True)),
                ("visible", models.BooleanField(db_index=True, default=True)),
                ("titulo", models.CharField(max_length=256)),
                ("description", models.CharField(max_length=600)),
                (
                    "anexo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="pqrs/%Y/",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("FN", "Finalizada"),
                            ("AC", "Activa"),
                            ("EP", "En espera"),
                        ],
                        default="AC",
                        max_length=10,
                    ),
                ),
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
            name="TipoPqrs",
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
                ("createdAt", models.DateField(auto_now_add=True, null=True)),
                ("updateAt", models.DateField(auto_now=True, null=True)),
                ("visible", models.BooleanField(db_index=True, default=True)),
                ("tipo", models.CharField(max_length=256)),
                (
                    "userCreate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "userUpdate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
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
                ("createdAt", models.DateField(auto_now_add=True, null=True)),
                ("updateAt", models.DateField(auto_now=True, null=True)),
                ("visible", models.BooleanField(db_index=True, default=True)),
                (
                    "anexo",
                    models.FileField(
                        blank=True, null=True, upload_to="pqrs/%Y/respuesta/"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=600, null=True),
                ),
                (
                    "pqrs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respuesta_pqrs",
                        to="pqrs.pqrs",
                    ),
                ),
                (
                    "userCreate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "userUpdate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Respuesta",
                "verbose_name_plural": "Respuestas",
            },
        ),
        migrations.AddField(
            model_name="pqrs",
            name="tipopqrs",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pqrs.tipopqrs"
            ),
        ),
        migrations.AddField(
            model_name="pqrs",
            name="userCreate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="pqrs",
            name="userUpdate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
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
                ("createdAt", models.DateField(auto_now_add=True, null=True)),
                ("updateAt", models.DateField(auto_now=True, null=True)),
                ("visible", models.BooleanField(db_index=True, default=True)),
                ("fecha_asignacion", models.DateField(auto_now=True)),
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
                (
                    "userCreate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "userUpdate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Asignacion",
                "verbose_name_plural": "Asignacions",
            },
        ),
        migrations.RunPython(
            insert_init_data, reverse_code=undo_insert_data, atomic=True
        ),
    ]
