from django.urls import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.university.headquartesr.route import Router
from apps.auth_module.api.view.university.headquartesr.views import SedeViewSet

router = Router()
router.register("", viewset=SedeViewSet, basename="sede")
urlpatterns = [path("", include(router.urls))]
