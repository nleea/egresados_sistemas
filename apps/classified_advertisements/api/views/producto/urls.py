from django.urls import path
from .view import DeleteSubCategoryView,SaveSubCategoryView,SubCategoryView,UpdateSubCategoryView

urlpatterns = [
    path("",SubCategoryView.as_view()),
    path("create/",SaveSubCategoryView.as_view()),
    path("update/<int:pk>/",UpdateSubCategoryView.as_view()),
    path("delete/<int:pk>/",DeleteSubCategoryView.as_view())
]
