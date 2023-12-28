from django.urls import path, re_path
# from .view import PqrsView

# app_name = "pqrs_module"

# urlpatterns = [
#     re_path(
#         r"(?P<status>)(?P<order>)(?P<startdate>)(?P<enddate>)$",
#         PqrsView.as_view(),
#     ),
# ]


from django.urls import path
from django.conf.urls import include
from src.application.pqrs.api.views.pqrs.router import Router
from src.application.pqrs.api.views.pqrs.view import PqrsViewSet

router = Router()
router.register("", viewset=PqrsViewSet, basename="pqrs")
urlpatterns = [path("", include(router.urls))]
