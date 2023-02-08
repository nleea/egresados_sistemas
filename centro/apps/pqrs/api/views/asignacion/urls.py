from django.urls import path
from .view import AsignacionView,SaveAsignacionView,UpdateAsignacionView

urlpatterns = [
    path("",AsignacionView.as_view()),
    path("create/",SaveAsignacionView.as_view()),
    path("update/<int:pk>/",UpdateAsignacionView.as_view())
]
