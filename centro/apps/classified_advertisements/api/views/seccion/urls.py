from django.urls import path
from .view import SaveSeccionView,SeccionView,UpdateSeccionView

urlpatterns = [
    path("",SeccionView.as_view()),
    path("create/",SaveSeccionView.as_view()),
    path("update/<int:pk>/",UpdateSeccionView.as_view())
]
