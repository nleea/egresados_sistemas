from django.urls import path
from .view import RespuestaView,SaveRespuestaView,UpdateRespuestaView

urlpatterns = [
    path("",RespuestaView.as_view()),
    path("create/",SaveRespuestaView.as_view()),
    path("update/<int:pk>/",UpdateRespuestaView.as_view())
]
