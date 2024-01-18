from src.interfaces.controllers.base_controller import BaseController
from rest_framework import status
from django.contrib.auth.models import Group, Permission
from django.db.models import Prefetch
from src.application.auth_module.models import Persons


class AuthModuleController(BaseController):
    def __init__(self, repo, serializer) -> None:
        super().__init__(repo, serializer)

    def post(self, data, extra=...):
        return super().post(data, extra)

    def get_roles(self, group):
        try:
            model_gestionar = [
                "eventosarea",
                "subareaeventos",
                "tipoevento",
                "asistencia",
                "tipomomento",
                "tipopqrs",
                "tipopqrs",
                "asignacion",
                "votoanuncio",
                "tiposcapacitaciones",
                "subcategoria",
                "redessociales",
                "genders",
                "faculties",
                "document_types",
                "programs",
                "headquarters",
                "user",
                "categoria",
                "question",
                "answer",
            ]

            group = Group.objects.prefetch_related(
                Prefetch(
                    "permissions",
                    Permission.objects.all().select_related("content_type"),
                ),
            ).get(pk=group)

            group_permissions = group.permissions.all()

            result_data = {"name": group.name, "permissions": {}}

            for permission in group_permissions:
                app_label = permission.content_type.app_label
                model = permission.content_type.model
                codename = permission.name

                if app_label not in result_data["permissions"]:
                    result_data["permissions"][app_label] = {}

                if model not in result_data["permissions"][app_label]:
                    if model in model_gestionar:
                        result_data["permissions"][app_label][model] = ["gestionar"]
                    else:
                        result_data["permissions"][app_label][model] = [codename]
                else:
                    if model not in model_gestionar:
                        result_data["permissions"][app_label][model].append(codename)

            return result_data, status.HTTP_200_OK
        except Group.DoesNotExist:
            return "Group not found", status.HTTP_404_NOT_FOUND
        except Exception as e:
            return str(e), status.HTTP_400_BAD_REQUEST

    def get_users(self, internal=True):
        queryset = (
            Persons.objects.select_related("user", "document_type", "gender_type")
            .prefetch_related(Prefetch("user__groups", Group.objects.all()))
            .filter(user__is_staff=internal)
        )

        list_user = []

        for i in queryset:
            user_groups = i.user.groups.values("name","id") if i.user else []
            list_user.append(
                {
                    "email": i.user.email if i.user else None,
                    "persona": {
                        "name": i.name,
                        "surname": i.surname,
                        "identification": i.identification,
                        "address": i.address,
                        "nationality": i.nationality,
                        "phone": i.phone,
                        "gender": i.gender_type.pk if i.gender_type else None,
                        "document": i.document_type.pk if i.document_type else None,
                    },
                    "groups": list(user_groups),
                }
            )

        return list_user, 200
