from django.urls import path
from .view import SaveSeccionView,SeccionView,UpdateSeccionView,DeleteSeccionView

urlpatterns = [
    path("",SeccionView.as_view()),
    path("create/",SaveSeccionView.as_view()),
    path("update/<int:pk>/",UpdateSeccionView.as_view()),
    path("delete/<int:pk>/",DeleteSeccionView.as_view())
]
