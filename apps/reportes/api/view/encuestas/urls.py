from django.urls import path,re_path
from .view import ReportesUserFacultaAndPrograma, ReportesUserFacultaWith

urlpatterns = [
    path("<slug:filter>/", ReportesUserFacultaAndPrograma.as_view()),
    path("respuesta/<slug:filter>/", ReportesUserFacultaWith.as_view()),
    path("respuesta/<slug:filter>/<int:facultad>/", ReportesUserFacultaWith.as_view()),
]
