from ..modules import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.resources.route import Router
from apps.auth_module.api.view.resources.views import ResourcesViewSet

router = Router()
router.register("", viewset=ResourcesViewSet, basename="resources")
urlpatterns = [path("", include(router.urls))]
