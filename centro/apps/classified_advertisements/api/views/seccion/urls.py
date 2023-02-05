from django.urls import path
<<<<<<< HEAD
from .view import SaveSeccionView,SeccionView,UpdateSeccionView

urlpatterns = [
    path("",SeccionView.as_view()),
    path("create/",SaveSeccionView.as_view()),
    path("update/<int:pk>/",UpdateSeccionView.as_view())
]
=======

urlpatterns = []
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
