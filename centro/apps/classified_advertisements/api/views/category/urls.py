from django.urls import path
from .view import CategoryView,SaveCategoryView,UpdateCategoryView

urlpatterns = [
    path("",CategoryView.as_view()),
    path("create/",SaveCategoryView.as_view()),
    path("update/<int:pk>/",UpdateCategoryView.as_view())
]
