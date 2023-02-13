from django.urls import path
from .view import RespuestaView,SaveRespuestaView,UpdateRespuestaView,DeleteRespuestaView

urlpatterns = [
    path("",RespuestaView.as_view()),
    path("create/",SaveRespuestaView.as_view()),
    path("update/<int:pk>/",UpdateRespuestaView.as_view()),
    path("delete/<int:pk>/",DeleteRespuestaView.as_view()),
]
