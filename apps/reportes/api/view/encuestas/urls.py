from django.urls import path
from .view import ReportesUserFaculta

urlpatterns = [path("faculta/", ReportesUserFaculta.as_view())]
