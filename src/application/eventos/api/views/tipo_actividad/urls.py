from django.urls import path
from django.conf.urls import include
from src.application.eventos.api.views.tipo_actividad.router import Router
from src.application.eventos.api.views.tipo_actividad.views import TipoViewSet

router = Router()
router.register("", viewset=TipoViewSet, basename="tipo_eventos")
urlpatterns = [path("", include(router.urls))]
