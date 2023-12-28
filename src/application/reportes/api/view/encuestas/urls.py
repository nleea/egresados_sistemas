from django.urls import path
from .view import ReportesUserFacultaAndPrograma, ReportesUserFacultaWith

urlpatterns = [
    path("respuesta/<slug:filter>/", ReportesUserFacultaAndPrograma.as_view()),
    path(
        "respuesta/<slug:filter>/<int:facultad>/",
        ReportesUserFacultaAndPrograma.as_view(),
    ),
    path("<slug:filter>/", ReportesUserFacultaWith.as_view()),
    path("<slug:filter>/<int:facultad>/", ReportesUserFacultaWith.as_view()),
    path(
        "<slug:filter>/<int:facultad>/<slug:generar>/",
        ReportesUserFacultaWith.as_view(),
    ),
    path(
        "<slug:filter>/<slug:grafica>/",
        ReportesUserFacultaWith.as_view(),
    ),
]
