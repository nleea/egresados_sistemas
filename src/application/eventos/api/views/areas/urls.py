from django.urls import path
from django.conf.urls import include

from src.application.eventos.api.views.areas.router import Router
from src.application.eventos.api.views.areas.views import AreasViewSet

router = Router()
router.register("", viewset=AreasViewSet, basename="areas")
urlpatterns = [
    path("", include(router.urls)),
]
