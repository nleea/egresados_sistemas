from django.urls import path

# urlpatterns = [
#     path("",CapacitacionesView.as_view()),
#     path("create/",SaveCapacitacionesView.as_view()),
#     path("update/<int:pk>/",UpdateCapacitacionesView.as_view()),
#     path("delete/",DeleteCapacitacionesView.as_view()),
#     path("delete/<int:pk>/",DeleteCapacitacionesView.as_view())
# ]

from django.conf.urls import include

from src.application.classified_advertisements.api.views.capacitaciones.router import Router
from src.application.classified_advertisements.api.views.capacitaciones.view import (
    CapacitacionesViewSet
)

router = Router()
router.register("", viewset=CapacitacionesViewSet, basename="capacitaciones")
urlpatterns = [path("", include(router.urls))]