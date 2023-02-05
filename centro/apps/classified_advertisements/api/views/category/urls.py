from django.urls import path
<<<<<<< HEAD
from .view import CategoryView,SaveCategoryView,UpdateCategoryView

urlpatterns = [
    path("",CategoryView.as_view()),
    path("create/",SaveCategoryView.as_view()),
    path("update/<int:pk>/",UpdateCategoryView.as_view())
]
=======

urlpatterns = []
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
