from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from ...serializers.resources.resources_serializers import (
    ResourcesRolesSerializers,
)
from rest_framework import status
from ....models import Resources, User, Resources_roles
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class SecurityResourcesCreate(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesRolesSerializers

    def post(self, request, *args, **kwargs):
        try:
            resources = ResourcesRolesSerializers(data=request.data)
            resources.is_valid(raise_exception=True)
            resources.save()
            return Response("Resources Create", status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


class SecurityRolesUser(APIView):
    def post(self, request, *args, **kwargs):
        user = request.data["user"]
        roles_id = request.data["roles"]
        roles = Group.objects.filter(id__in=roles_id)

        try:
            if roles:
                User.objects.get(pk=user).groups.set([x.pk for x in roles])
            return Response("Success", status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)


#@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class PermissionsView(APIView):
    def get(self, request, *args, **kwargs):
        excluded_apps = {
            "admin",
            "auth",
            "contenttypes",
            "sessions",
            "authtoken",
            "token_blacklist",
            "resources_roles",
            "persons",
            "resources",
            "respuesta",
            "redessociales",
            "votoanuncio",
            "mensajes",
            "answeruser",
            "inscripcion",
        }

        content_types = ContentType.objects.exclude(
            Q(model__in=excluded_apps) | Q(app_label__in=excluded_apps)
        ).values("app_label", "model")
        permissions_data = {}

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

        for content_type in content_types:
            app_label = content_type["app_label"]
            model = content_type["model"]

            if model in model_gestionar:
                permissions_data.setdefault(app_label, {})[model] = ["gestionar"]
            else:
                permissions_data.setdefault(app_label, {})[model] = [
                    permission.name
                    for permission in Permission.objects.filter(
                        content_type__model=model
                    )
                ]

        permissions_data.setdefault("admin", {})["roles"] = ["gestionar"]
        permissions_data.setdefault("classified_advertisements", {})["detalles"] = [
            "gestionar"
        ]

        return Response(permissions_data, status=status.HTTP_200_OK)

    def insert_update_roles(self, data, role):
        try:
            data_permissions = data.get("permissions", {})
            role_name = data.get("role", None)

            if role_name is None:
                return Response("Fields Required", status=status.HTTP_400_BAD_REQUEST)

            instance_permissions = []

            for permission_data in data_permissions.keys():
                name = permission_data
                permissions = data_permissions[name]

                if permissions == []:
                    continue

                if permissions[0] == "gestionar" and name == "roles":
                    instance_permissions.extend(
                        Permission.objects.filter(content_type__app_label="auth")
                    )
                elif permissions[0] == "gestionar" and name == "detalles":
                    instance_permissions.extend(
                        Permission.objects.filter(
                            Q(content_type__model="anuncio")
                            | Q(content_type__model="mensajes")
                        )
                    )
                elif permissions[0] == "gestionar":
                    instance_permissions.extend(
                        Permission.objects.filter(content_type__model=name)
                    )
                else:
                    instance_permissions.extend(
                        Permission.objects.filter(
                            content_type__model=name, name__in=permissions
                        )
                    )

            role.permissions.set(instance_permissions)

            return "Ok", status.HTTP_200_OK
        except Exception as e:
            return e.args, status.HTTP_400_BAD_REQUEST

    def post(self, request, *args, **kwargs):
        role_name = request.data.get("role", "")
        role, _ = Group.objects.get_or_create(name=role_name)
        response, status = self.insert_update_roles(request.data, role)
        return Response(response, status)

    def put(self, request, *args, **kwargs):
        role_name = request.data.get("role", "")
        role = request.data.get("id", "")

        role = Group.objects.get(pk=role)
        response, status = self.insert_update_roles(request.data, role)

        if role_name != role.name:
            role.name = role_name
            role.save()

        return Response(response, status)


class CheckPermissions(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        permissions = request.data["permissions"]
        check_resulst = user.has_perms(permissions)

        return Response({"valid": check_resulst}, status=status.HTTP_200_OK)


#@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class ResourcesView(APIView):
    def get(self, request, *args, **kwargs):
        resources = Resources.objects.all().order_by("id_padre", "id")

        arbol = {}
        padres = {}

        items = [
            {"id_padre": x.id_padre, "id": x.pk, "titulo": x.titulo, "path": x.path}
            for x in resources
        ]

        for item in items:
            if item["id_padre"] == 0:
                arbol[item["id"]] = item
            else:
                padre_id = item["id_padre"]
                if padre_id not in padres:
                    padres[padre_id] = []
                padres[padre_id].append(item)

        for item in items:
            item_id = item["id"]
            if item_id in padres:
                item["children"] = padres[item_id]

        arbol_list = [x for x in arbol.values()]

        return Response(arbol_list, status=status.HTTP_200_OK)


class ResourcesRolesView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            rol = request.data.get("rol", None)
            resources = request.data.get("resources")

            if not rol:
                return Response("Rol es requerido", status=status.HTTP_400_BAD_REQUEST)

            roles_resource = [
                Resources_roles(rolesId__id=rol, resourcesId__id=x) for x in resources
            ]

            Resources_roles.objects.bulk_create(roles_resource)
            return Response("Ok", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)
