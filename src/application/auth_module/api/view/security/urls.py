from django.urls import path

from .security import SecurityResourcesCreate, SecurityRolesUser,CheckPermissions

urlpatterns = [
    path('create/roles/resources/', SecurityResourcesCreate.as_view()),
    path('create/roles/user/', SecurityRolesUser.as_view()),
    path('check/roles/permission/', CheckPermissions.as_view())
]
