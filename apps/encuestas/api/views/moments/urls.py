from django.urls import path
from django.conf.urls import include
from apps.encuestas.api.views.moments.router import Router
from apps.encuestas.api.views.moments.view import MomentsViewSet

router = Router()
router.register("", viewset=MomentsViewSet, basename="moments")
urlpatterns = [path("", include(router.urls))]
