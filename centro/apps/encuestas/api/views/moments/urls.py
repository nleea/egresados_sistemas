from django.urls import path
from .view import MomentView,SaveMomentsView,UpdateMomentsView,DeleteMomentsView

urlpatterns = [
    path("",MomentView.as_view()),
    path("create/",SaveMomentsView.as_view()),
    path("update/<int:pk>/",UpdateMomentsView.as_view()),
    path("delete/<int:pk>/",DeleteMomentsView.as_view()),    
]
