from django.urls import path
from .view import SaveSubCategoryView,UpdateSubCategoryView,SubCategoryView,DeleteSubcategoryView

urlpatterns = [
    path("",SubCategoryView.as_view()),
    path("create/",SaveSubCategoryView.as_view()),
    path("update/<int:pk>/",UpdateSubCategoryView.as_view()),
    path("delete/<int:pk>/",DeleteSubcategoryView.as_view())
]
