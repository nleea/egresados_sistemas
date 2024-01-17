from django.urls import path

from .security import (
    SecurityResourcesCreate,
    SecurityRolesUser,
    CheckPermissions,
    PermissionsView,
    ResourcesView
)

urlpatterns = [
    path("create/roles/resources/", SecurityResourcesCreate.as_view()),
    path("create/roles/user/", SecurityRolesUser.as_view()),
    path("check/roles/permission/", CheckPermissions.as_view()),
    path("roles/permission/", PermissionsView.as_view()),
    path("roles/resources/", ResourcesView.as_view())
]
