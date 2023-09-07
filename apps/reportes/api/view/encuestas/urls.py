from django.urls import path,re_path
from .view import ReportesUserFaculta, ReportesUserFacultaWith

urlpatterns = [
    path("faculta/", ReportesUserFaculta.as_view()),
    path("respuesta/<slug:filter>/", ReportesUserFacultaWith.as_view()),
    path("respuesta/<slug:filter>/<int:facultad>/", ReportesUserFacultaWith.as_view()),
]
