from django.urls import path

# from .view import (
#     RespuestaView,
#     SaveRespuestaView,
#     UpdateRespuestaView,
#     DeleteRespuestaView,
#     RespuestasQuery,
# )

# app_name = "respuesta"

# urlpatterns = [
#     path("", RespuestaView.as_view(), name="respuesta-list"),
#     path("create/", SaveRespuestaView.as_view(), name="respuesta-create"),
#     path("update/<int:pk>/", UpdateRespuestaView.as_view()),
#     path("delete/<int:pk>/", DeleteRespuestaView.as_view()),
#     path("delete/", DeleteRespuestaView.as_view()),
#     path("query/", RespuestasQuery.as_view()),
# ]

from django.conf.urls import include
from apps.pqrs.api.views.respuesta.router import Router
from apps.pqrs.api.views.respuesta.view import RespuestaViewSet

router = Router()
router.register("", viewset=RespuestaViewSet, basename="respuestas")
urlpatterns = [path("", include(router.urls))]
