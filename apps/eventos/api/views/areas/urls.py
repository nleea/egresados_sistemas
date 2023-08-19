from django.urls import path
from .views import (
    DeleteEventosAreaView,
    EventosAreaView,
    SaveEventosAreaView,
    UpdateEventosAreaView,
)

app_name = "areas"

urlpatterns = [
    path("", EventosAreaView.as_view(), name="areas-list"),
    path("create/", SaveEventosAreaView.as_view()),
    path("update/<int:pk>/", UpdateEventosAreaView.as_view()),
    path("delete/<int:pk>/", DeleteEventosAreaView.as_view()),
    path("delete/", DeleteEventosAreaView.as_view()),
]
