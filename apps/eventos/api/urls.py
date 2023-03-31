from django.urls import path, include

urlpatterns = [
    path("", include("apps.eventos.api.views.eventos.urls"))
]
