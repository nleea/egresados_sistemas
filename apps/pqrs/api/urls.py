from django.urls import path, re_path, include

app_name = "pqrs"

urlpatterns = [
    re_path(r"^", include("apps.pqrs.api.views.pqrs.urls"), name="pqrs-url"),
    path(
        "asignacion/",
        include("apps.pqrs.api.views.asignacion.urls"),
        name="asignacion-url",
    ),
    path("respuesta/", include("apps.pqrs.api.views.respuesta.urls"), name="respuesta"),
    path("tipo/", include("apps.pqrs.api.views.tipoPqrs.urls"), name="tipo"),
]
