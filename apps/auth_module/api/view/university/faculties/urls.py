from django.urls import path
from .views import DeleteFacultiesView,SaveFacultiesView,UpdateFacultiesAreaView,FacultiesView

urlpatterns = [
    path("", FacultiesView.as_view()),
    path("create/", SaveFacultiesView.as_view()),
    path("update/<int:pk>/", UpdateFacultiesAreaView.as_view()),
    path("delete/<int:pk>/", DeleteFacultiesView.as_view())
]
