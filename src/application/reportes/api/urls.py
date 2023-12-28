from django.urls import path, include
from src.application.constants import PATH_APP

urlpatterns = [
    path("encuestas/", include(f"{PATH_APP}.reportes.api.view.encuestas.urls"))
]
