# Generated by Django 4.1.2 on 2022-11-11 22:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from ...helpers import menu
from ...helpers.menu_resources import menuResources
from django.contrib.auth.hashers import make_password

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    def insert_init_data(apps, schema_editor):
        User = apps.get_model('auth_module', 'User')
        User.objects.bulk_create(
            [User(
                username='admin', email='admin@gmail.com', password=make_password('12345678'), is_staff=True),
             User(
                username='egresado', email='egresado@gmail.com', password=make_password('12345678'))])

        Roles = apps.get_model('auth_module', 'Roles')
        Roles.objects.bulk_create(
            [Roles(name='Admin', status=True), Roles(name='Egresado', status=True)])

        User_roles = apps.get_model('auth_module', 'User_roles')
        User_roles.objects.bulk_create(
            [User_roles(userId=User.objects.get(pk=1), rolesId=Roles.objects.get(pk=1)), User_roles(userId=User.objects.get(pk=1), rolesId=Roles.objects.get(pk=2))])

        Resources = apps.get_model('auth_module', 'Resources')
        resources = []
        menuResources(menu.resources, resources, Resources, 0)
        resources = Resources.objects.bulk_create(resources)

        Resources_roles = apps.get_model('auth_module', 'Resources_roles')
        list_resources_roles = []
        rol = Roles.objects.get(pk=1)
        for r in resources:
            list_resources_roles.append(Resources_roles(
                rolesId=rol, resourcesId=r))
        Resources_roles.objects.bulk_create(list_resources_roles)

    def undo_insert_data(apps, schema_editor):
        User_roles = apps.get_model('auth_module', 'User_roles')
        User_roles.objects.all().delete()
        Roles = apps.get_model('auth_module', 'Roles')
        Roles.objects.all().delete()
        User = apps.get_model('auth_module', 'User')
        User.objects.all().delete()
        Resources_roles = apps.get_model('auth_module', 'Resources_roles')
        Resources_roles.objects.all().delete()
        Resources = apps.get_model('auth_module', 'Resources')
        Resources.objects.all().delete()

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=254,
                 unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100)),
                ('resetToken', models.CharField(
                    blank=True, max_length=256, null=True)),
                ('avatar', models.CharField(blank=True, max_length=256, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Document_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Document_types',
                'verbose_name_plural': 'Document_types',
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Genders',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('path', models.CharField(max_length=256)),
                ('id_padre', models.IntegerField()),
                ('method', models.CharField(max_length=256)),
                ('icono', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Resources',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='Resources_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('resourcesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='resources', to='auth_module.resources')),
            ],
            options={
                'verbose_name': 'Resources_roles',
                'verbose_name_plural': 'Resources_roles',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('resources', models.ManyToManyField(related_name='roles_resources',
                 through='auth_module.Resources_roles', to='auth_module.resources')),
            ],
            options={
                'verbose_name': 'Roles',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='User_roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('rolesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='roles', to='auth_module.roles')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_roles',
                'verbose_name_plural': 'user_roles',
            },
        ),
        migrations.AddField(
            model_name='roles',
            name='users',
            field=models.ManyToManyField(
                related_name='roles_user', through='auth_module.User_roles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resources_roles',
            name='rolesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='resouces_roles', to='auth_module.roles'),
        ),
        migrations.AddField(
            model_name='resources',
            name='roles',
            field=models.ManyToManyField(
                related_name='resources_roles', through='auth_module.Resources_roles', to='auth_module.roles'),
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('identification', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=30)),
                ('date_of_birth', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='document_types', to='auth_module.document_types')),
                ('gender_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='gender_types', to='auth_module.genders')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(
                related_name='user_roles', through='auth_module.User_roles', to='auth_module.roles'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set',
                                         related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.RunPython(insert_init_data, reverse_code=undo_insert_data)
    ]
