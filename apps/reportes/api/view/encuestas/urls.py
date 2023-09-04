from django.urls import path
from .view import ReportesUserFaculta, ReportesUser

urlpatterns = [
    path("faculta/", ReportesUserFaculta.as_view()),
    path("respuesta/", ReportesUser.as_view()),
]
