from django.urls import path

from .security import SecurityResourcesCreate

urlpatterns = [
    path('create/roles/resources/', SecurityResourcesCreate.as_view())
]
