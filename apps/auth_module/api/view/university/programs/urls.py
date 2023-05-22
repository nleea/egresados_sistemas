from django.urls import path
from .views import DeleteProgramsView,ProgramsView,SaveProgramsView,UpdateProgramsView

urlpatterns = [
    path("", ProgramsView.as_view()),
    path("create/", SaveProgramsView.as_view()),
    path("update/<int:pk>/", UpdateProgramsView.as_view()),
    path("delete/<int:pk>/", DeleteProgramsView.as_view()),
    path("delete/", DeleteProgramsView.as_view())
]
