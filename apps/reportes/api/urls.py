from django.urls import path, include

urlpatterns = [
    path("encuestas/",include("apps.reportes.api.view.encuestas.urls"))
]
