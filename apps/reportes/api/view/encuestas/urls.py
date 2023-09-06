from django.urls import path
from .view import ReportesUserFaculta, ReportesUser, ReportesUserFacultaWith

urlpatterns = [
    path("faculta/", ReportesUserFaculta.as_view()),
    path("respuesta/<slug:filter>", ReportesUserFacultaWith.as_view()),
]
