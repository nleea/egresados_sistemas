from django.urls import path
from .view import (
    AsignacionView,
    SaveAsignacionView,
    UpdateAsignacionView,
    DeleteAsignacionView,
    AsignacionPqrsView,
)

app_name = "asignacion"

urlpatterns = [
    path("", AsignacionView.as_view(), name="asignacion-view"),
    path("solicitudes/", AsignacionPqrsView.as_view(), name="asignacion-solicitudes"),
    path("create/", SaveAsignacionView.as_view(), name="asignacion-create"),
    path("update/<int:pk>/", UpdateAsignacionView.as_view()),
    path("delete/<int:pk>/", DeleteAsignacionView.as_view()),
    path("delete/", DeleteAsignacionView.as_view()),
]
