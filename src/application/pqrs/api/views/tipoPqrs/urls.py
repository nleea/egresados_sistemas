from django.urls import path
from django.conf.urls import include
from src.application.pqrs.api.views.tipoPqrs.router import Router
from src.application.pqrs.api.views.tipoPqrs.view import TipoViewSet

router = Router()
router.register("", viewset=TipoViewSet, basename="tipo_pqrs")
urlpatterns = [path("", include(router.urls))]
