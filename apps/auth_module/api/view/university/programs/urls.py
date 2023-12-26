
from django.urls import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.university.programs.route import Router
from apps.auth_module.api.view.university.programs.views import ProgramaViewSet

router = Router()
router.register("", viewset=ProgramaViewSet, basename="programa")
urlpatterns = [path("", include(router.urls))]
