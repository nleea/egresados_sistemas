from django.urls import path, include, re_path
from src.application.constants import PATH_APP

app_name = "eventos"

urlpatterns = [
    path("", include(f"{PATH_APP}.eventos.api.views.eventos.urls")),
    path("areas/", include(f"{PATH_APP}.eventos.api.views.areas.urls")),
    path("sub/areas/", include(f"{PATH_APP}.eventos.api.views.subAreas.urls")),
    path("tipos/", include(f"{PATH_APP}.eventos.api.views.tipo_actividad.urls")),
    re_path(
        "inscripciones/", include(f"{PATH_APP}.eventos.api.views.incripciones.urls")
    ),
]
