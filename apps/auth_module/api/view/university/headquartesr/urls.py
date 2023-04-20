from django.urls import path
from .views import DeleteHeadquartersView, HeadquartersView, SaveHeadquartersView, UpdateHeadquartersView

urlpatterns = [
    path("", HeadquartersView.as_view()),
    path("create/", SaveHeadquartersView.as_view()),
    path("update/<int:pk>/", UpdateHeadquartersView.as_view()),
    path("delete/<int:pk>/", DeleteHeadquartersView.as_view())
]
