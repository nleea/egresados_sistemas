from django.urls import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.university.faculties.route import Router
from apps.auth_module.api.view.university.faculties.views import FacultyViewSet

router = Router()
router.register("", viewset=FacultyViewSet, basename="facultad")
urlpatterns = [path("", include(router.urls))]
