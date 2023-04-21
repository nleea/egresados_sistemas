from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("apps.pqrs.api.views.pqrs.urls")),
    path("asignacion/", include("apps.pqrs.api.views.asignacion.urls")),
    path("respuesta/", include("apps.pqrs.api.views.respuesta.urls")),
    path("tipo/", include("apps.pqrs.api.views.tipoPqrs.urls")),
]
