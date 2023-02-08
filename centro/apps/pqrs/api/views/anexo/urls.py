from django.urls import path
from .view import AnexoView,SaveAnexoView,UpdateAnexoView

urlpatterns = [
    path("",AnexoView.as_view()),
    path("create/",SaveAnexoView.as_view()),
    path("update/<int:pk>/",UpdateAnexoView.as_view())
]
