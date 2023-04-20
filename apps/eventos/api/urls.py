from django.urls import path, include

urlpatterns = [
    path("", include("apps.eventos.api.views.eventos.urls")),
    path("areas/", include("apps.eventos.api.views.areas.urls")),
    path("sub/areas/", include("apps.eventos.api.views.subAreas.urls")),
    path("tipos/", include("apps.eventos.api.views.tipo_actividad.urls"))
]
