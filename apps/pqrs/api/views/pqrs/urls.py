from django.urls import path, re_path
from .view import PqrsView, SavePqrsView, UpdatePqrsView, DeletePqrsView

app_name = "pqrs_module"

urlpatterns = [
    re_path(
        r"(?P<status>)(?P<order>)(?P<startdate>)(?P<enddate>)$",
        PqrsView.as_view(),
    ),
    path("test/", PqrsView.as_view(), name="list-pqrs"),
    path("create/", SavePqrsView.as_view(), name="create-pqrs"),
    path("update/<int:pk>/", UpdatePqrsView.as_view()),
    path("delete/<int:pk>/", DeletePqrsView.as_view()),
    path("delete/", DeletePqrsView.as_view()),
]
