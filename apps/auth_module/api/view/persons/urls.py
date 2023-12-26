from ..modules import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.persons.route import Router
from apps.auth_module.api.view.persons.persons import PersonViewSet

router = Router()
router.register("", viewset=PersonViewSet, basename="person")
urlpatterns = [path("", include(router.urls))]
