from django.urls import path
<<<<<<< HEAD
from .view import SaveSubCategoryView,UpdateSubCategoryView,SubCategoryView

urlpatterns = [
    path("",SubCategoryView.as_view()),
    path("create/",SaveSubCategoryView.as_view()),
    path("update/<int:pk>/",UpdateSubCategoryView.as_view())
]
=======

urlpatterns = []
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
