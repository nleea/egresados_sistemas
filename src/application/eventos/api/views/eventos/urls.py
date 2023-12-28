from django.urls import path
from .views import (
    SaveEventosView,
    EventosTe,
)

from django.conf.urls import include

from src.application.eventos.api.views.eventos.router import Router
from src.application.eventos.api.views.eventos.views import EventosViewSet

router = Router()
router.register("", viewset=EventosViewSet, basename="eventos")
urlpatterns = [
    path("", include(router.urls)),
    path("create/", SaveEventosView.as_view()),
    path("template/", EventosTe.as_view()),
]
