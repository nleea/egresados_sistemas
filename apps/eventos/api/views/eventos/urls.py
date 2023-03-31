from django.urls import path
from .views import DeleteEventosView, SaveEventosView, EventosView, UpdateEventosView

urlpatterns = [
    path("", EventosView.as_view()),
    path("create/", SaveEventosView.as_view()),
    path("update/<int:pk>/", UpdateEventosView.as_view()),
    path("delete/<int:pk>/", DeleteEventosView.as_view())
]
