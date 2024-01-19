from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.utils import timezone

from .managers.users.managers import UserManagers
from src.application.default.models import BaseModel

class Document_types(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Document_types"
        verbose_name_plural = "Document_types"


class Genders(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Genders"
        verbose_name_plural = "Genders"


class User(AbstractUser, BaseModel):
    username = models.CharField(blank=False, null=False, unique=True, max_length=256)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    password = models.CharField(max_length=100)
    resetToken = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    roles = models.ManyToManyField(Group, related_name="user_roles", db_index=True)

    # objects = UserManager()
    objects = UserManagers()

    class Meta:
        # unique_together = (('username', 'email'))
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username


# class Roles(BaseModel):
#     name = models.CharField(max_length=200, unique=True)
#     status = models.BooleanField(default=True)
#     users = models.ManyToManyField(
#         User, through='User_roles', related_name='roles_user')
#     resources = models.ManyToManyField(
#         'Resources', through='Resources_roles', related_name='roles_resources')

#     def __str__(self) -> str:
#         return self.name

#     class Meta:
#         verbose_name = 'Roles'
#         verbose_name_plural = 'Roles'


class Persons(BaseModel):
    name = models.CharField(max_length=150, unique=True, blank=True, null=True)
    surname = models.CharField(max_length=150, unique=False, blank=True, null=True)
    identification = models.CharField(max_length=40, unique=True, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=False, null=False, default=timezone.now().date())
    phone = models.CharField(max_length=11, blank=True, null=True)
    status = models.BooleanField(default=True)
    document_type = models.ForeignKey(
        Document_types, on_delete=models.SET_NULL, blank=True, null=True
    )
    gender_type = models.ForeignKey(
        Genders,
        related_name="gender_types",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, db_index=True
    )
    program = models.ForeignKey(
        "Programs", on_delete=models.CASCADE, null=True, db_index=True
    )

    def __str__(self) -> str:
        return self.name  # type: ignore

    class Meta:
        unique_together = ("name", "identification")
        verbose_name = "Persons"
        verbose_name_plural = "Persons"


# class User_roles(BaseModel):
#     status = models.BooleanField(default=True)
#     userId = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='users')
#     rolesId = models.ForeignKey(
#         Group, on_delete=models.CASCADE, related_name='roles')

#     def __str__(self) -> str:
#         return self.userId.username + '-' + self.rolesId.name

#     class Meta:
#         unique_together = (('userId', 'rolesId'))
#         verbose_name = 'User_roles'
#         verbose_name_plural = 'user_roles'


class Resources(BaseModel):
    path = models.CharField(max_length=256)
    id_padre = models.IntegerField()
    method = models.CharField(max_length=256)
    icono = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    titulo = models.CharField(max_length=100)
    roles = models.ManyToManyField(
        Group, through="Resources_roles", related_name="resources_roles", db_index=True
    )

    class Meta:
        verbose_name = "Resources"
        verbose_name_plural = "Resources"


class Resources_roles(BaseModel):
    resourcesId = models.ForeignKey(
        Resources, on_delete=models.CASCADE, related_name="resources"
    )
    rolesId = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="resouces_roles"
    )

    def __str__(self) -> str:
        return self.resourcesId.path + "" + self.rolesId.name

    class Meta:
        verbose_name = "Resources_roles"
        verbose_name_plural = "Resources_roles"


class Headquarters(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Headquarter"
        verbose_name_plural = "Headquarters"


class Faculties(BaseModel):
    name = models.CharField(max_length=256)
    headquarter = models.ForeignKey(Headquarters, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Facultie"
        verbose_name_plural = "Faculties"


class Programs(BaseModel):
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"
