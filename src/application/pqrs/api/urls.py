from django.urls import path, re_path, include
from src.application.constants import PATH_APP

app_name = "pqrs"

urlpatterns = [
    re_path(r"^", include(f"{PATH_APP}.pqrs.api.views.pqrs.urls"), name="pqrs-url"),
    path(
        "asignacion/",
        include(f"{PATH_APP}.pqrs.api.views.asignacion.urls"),
        name="asignacion-url",
    ),
    path(
        "respuesta/",
        include(f"{PATH_APP}.pqrs.api.views.respuesta.urls"),
        name="respuesta",
    ),
    path("tipo/", include(f"{PATH_APP}.pqrs.api.views.tipoPqrs.urls"), name="tipo"),
]
