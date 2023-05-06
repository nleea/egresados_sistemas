from django.urls import path,re_path
from .view import InscripcionView,IncripcionSave,AsistenciaView

urlpatterns = [
    re_path(r'^(?P<evento>\w{0,50})$', InscripcionView.as_view()),
    path("save/", IncripcionSave.as_view()),
    re_path(r'^asistencia/(?P<evento>\w{0,50})/(?P<user>\w{0,50})$', AsistenciaView.as_view()),
    
]