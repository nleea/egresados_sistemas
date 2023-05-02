from django.urls import path
from .view import InscripcionView,IncripcionSave

urlpatterns = [
    path("", InscripcionView.as_view()),
    path("save/", IncripcionSave.as_view())
    
]
