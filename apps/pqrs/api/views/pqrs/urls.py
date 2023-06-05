from django.urls import path,re_path
from .view import PqrsView,SavePqrsView,UpdatePqrsView,DeletePqrsView

urlpatterns = [
    re_path(r"(?P<status>)(?P<order>)(?P<startdate>)(?P<enddate>)$",PqrsView.as_view()),
    path("create/",SavePqrsView.as_view()),
    path("update/<int:pk>/",UpdatePqrsView.as_view()),
    path("delete/<int:pk>/",DeletePqrsView.as_view()),
    path("delete/",DeletePqrsView.as_view()),
]
