# Generated by Django 4.1.2 on 2023-12-23 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100)),
                ('resetToken', models.CharField(blank=True, max_length=256, null=True)),
                ('avatar', models.CharField(blank=True, max_length=256, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('roles', models.ManyToManyField(db_index=True, related_name='user_roles', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Document_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Document_types',
                'verbose_name_plural': 'Document_types',
            },
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Facultie',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Genders',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Headquarters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Headquarter',
                'verbose_name_plural': 'Headquarters',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('resourcesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='auth_module.resources')),
                ('rolesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resouces_roles', to='auth.group')),
            ],
            options={
                'verbose_name': 'Resources_roles',
                'verbose_name_plural': 'Resources_roles',
            },
        ),
        migrations.AddField(
            model_name='resources',
            name='roles',
            field=models.ManyToManyField(db_index=True, related_name='resources_roles', through='auth_module.Resources_roles', to='auth.group'),
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=256)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_module.faculties')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.AddField(
            model_name='faculties',
            name='headquarter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_module.headquarters'),
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('surname', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('identification', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('status', models.BooleanField(default=True)),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_module.document_types')),
                ('gender_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gender_types', to='auth_module.genders')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_module.programs')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Persons',
                'verbose_name_plural': 'Persons',
                'unique_together': {('name', 'identification')},
            },
        ),
    ]