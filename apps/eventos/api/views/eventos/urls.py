from django.urls import path,re_path
from .views import DeleteEventosView, SaveEventosView, EventosView, UpdateEventosView

urlpatterns = [
    re_path(r"(?P<mine>)$", EventosView.as_view()),
    path("create/", SaveEventosView.as_view()),
    path("update/<int:pk>/", UpdateEventosView.as_view()),
    path("delete/<int:pk>/", DeleteEventosView.as_view()),
    path("delete/", DeleteEventosView.as_view())
]
