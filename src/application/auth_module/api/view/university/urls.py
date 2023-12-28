from django.urls import path, include
from src.application.constants import PATH_APP

urlpatterns = [
    path("faculta/", include(f"{PATH_APP}.auth_module.api.view.university.faculties.urls")),
    path("sede/", include(f"{PATH_APP}.auth_module.api.view.university.headquartesr.urls")),
    path("programa/", include(f"{PATH_APP}.auth_module.api.view.university.programs.urls")),
]
