from django.urls import path
from .view import MomentView,SaveMomentsView,UpdateMomentsView

urlpatterns = [
    path("",MomentView.as_view()),
    path("create/",SaveMomentsView.as_view()),
    path("update/<int:pk>/",UpdateMomentsView.as_view())
]
