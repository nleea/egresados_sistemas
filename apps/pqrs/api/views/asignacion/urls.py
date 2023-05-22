from django.urls import path
from .view import AsignacionView, SaveAsignacionView, UpdateAsignacionView, DeleteAsignacionView, AsignacionPqrsView

urlpatterns = [
    path("", AsignacionView.as_view()),
    path("solicitudes/", AsignacionPqrsView.as_view()),
    path("create/", SaveAsignacionView.as_view()),
    path("update/<int:pk>/", UpdateAsignacionView.as_view()),
    path("delete/<int:pk>/", DeleteAsignacionView.as_view()),
    path("delete/", DeleteAsignacionView.as_view()),

]
