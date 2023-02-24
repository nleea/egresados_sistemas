from django.urls import path
from .view import CategoryView,SaveCategoryView,UpdateCategoryView,DeleteCategoriaView

urlpatterns = [
    path("",CategoryView.as_view()),
    path("create/",SaveCategoryView.as_view()),
    path("update/<int:pk>/",UpdateCategoryView.as_view()),
    path("delete/<int:pk>/",DeleteCategoriaView.as_view())
]
