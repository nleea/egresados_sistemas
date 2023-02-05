from django.urls import path
from .view import SaveSubCategoryView,UpdateSubCategoryView,SubCategoryView

urlpatterns = [
    path("",SubCategoryView.as_view()),
    path("create/",SaveSubCategoryView.as_view()),
    path("update/<int:pk>/",UpdateSubCategoryView.as_view())
]
