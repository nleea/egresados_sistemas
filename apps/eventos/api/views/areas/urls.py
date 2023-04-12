from django.urls import path
from .views import DeleteEventosAreaView, EventosAreaView, SaveEventosAreaView, UpdateEventosAreaView

urlpatterns = [
    path("", EventosAreaView.as_view()),
    path("create/", SaveEventosAreaView.as_view()),
    path("update/<int:pk>/", UpdateEventosAreaView.as_view()),
    path("delete/<int:pk>/", DeleteEventosAreaView.as_view())
]
