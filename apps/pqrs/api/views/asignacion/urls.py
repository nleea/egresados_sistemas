# from django.urls import path
# from .view import (
#     AsignacionView,
#     SaveAsignacionView,
#     UpdateAsignacionView,
#     DeleteAsignacionView,
#     AsignacionPqrsView,
# )

# app_name = "asignacion"

# urlpatterns = [
#     path("", AsignacionView.as_view(), name="asignacion-view"),
#     path("solicitudes/", AsignacionPqrsView.as_view(), name="asignacion-solicitudes"),
#     path("create/", SaveAsignacionView.as_view(), name="asignacion-create"),
#     path("update/<int:pk>/", UpdateAsignacionView.as_view()),
#     path("delete/<int:pk>/", DeleteAsignacionView.as_view()),
#     path("delete/", DeleteAsignacionView.as_view()),
# ]


from django.urls import path
from django.conf.urls import include
from apps.pqrs.api.views.asignacion.router import Router
from apps.pqrs.api.views.asignacion.view import AsignacionViewSet

router = Router()
router.register("", viewset=AsignacionViewSet, basename="asignacion")
urlpatterns = [path("", include(router.urls))]
