from django.urls import path
<<<<<<< HEAD
from .view import SaveSubCategoryView,UpdateSubCategoryView,SubCategoryView,DeleteSubCategoryView
=======
from .view import SaveSubCategoryView,UpdateSubCategoryView,SubCategoryView,DeleteSubcategoryView
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345

urlpatterns = [
    path("",SubCategoryView.as_view()),
    path("create/",SaveSubCategoryView.as_view()),
    path("update/<int:pk>/",UpdateSubCategoryView.as_view()),
<<<<<<< HEAD
    path("delete/<int:pk>/",DeleteSubCategoryView.as_view())
=======
    path("delete/<int:pk>/",DeleteSubcategoryView.as_view())
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345
]
