from django.urls import path,re_path
from .view import InscripcionView,IncripcionSave

urlpatterns = [
    re_path(r'^(?P<evento>\w*)', InscripcionView.as_view()),
    path("save/", IncripcionSave.as_view())
    
]
