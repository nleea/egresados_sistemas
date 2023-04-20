from django.urls import path, include

urlpatterns = [
    path("faculta/", include("apps.auth_module.api.view.university.faculties.urls")),
    path("sede/", include("apps.auth_module.api.view.university.headquartesr.urls")),
    path("programa/", include("apps.auth_module.api.view.university.programs.urls")),

]
