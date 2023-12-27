from django.urls import path
from django.conf.urls import include
from apps.classified_advertisements.api.views.category.router import Router
from apps.classified_advertisements.api.views.category.view import CategoryViewSet

router = Router()
router.register("", viewset=CategoryViewSet, basename="categoria")
urlpatterns = [path("", include(router.urls))]
