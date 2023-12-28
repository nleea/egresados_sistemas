from django.urls import path


from django.conf.urls import include
from django.urls import path


from src.application.auth_module.api.view.roles.route import Router
from src.application.auth_module.api.view.roles.views import RoleViewSet

router = Router()
router.register("", viewset=RoleViewSet, basename="roles")
urlpatterns = [path("", include(router.urls))]
