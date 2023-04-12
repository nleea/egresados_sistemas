from django.urls import path
from .views import DeleteEventosSubAreaView, SaveEventosSubAreaView, UpdateEventosSubAreaView, EventosSubAreaView, EventosQuery

urlpatterns = [
    path("", EventosSubAreaView.as_view()),
    path("create/", SaveEventosSubAreaView.as_view()),
    path("update/<int:pk>/", UpdateEventosSubAreaView.as_view()),
    path("delete/<int:pk>/", DeleteEventosSubAreaView.as_view()),
    path("query/", EventosQuery.as_view())
]
