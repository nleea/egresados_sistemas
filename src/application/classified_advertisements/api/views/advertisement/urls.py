from django.urls import path, re_path

# from .views import (
#     AdvertisementView,
#     SaveAdvertisementView,
#     DeleteCategoryView,
#     UpdateCategoryView,
#     AdvertisementsQueryView,
#     MyAdvertisementView,
#     SaveAdvertisementVoto,
#     AdvertisementMostVoteView,
#     AdvertisementStateChangeView,
# )

# urlpatterns = [
#     re_path(r"(?P<subCategoryId>\w{0,50})$", AdvertisementView.as_view()),
#     path("mine/", MyAdvertisementView.as_view()),
#     path("create/", SaveAdvertisementView.as_view()),
#     path("update/<int:pk>/", UpdateCategoryView.as_view()),
#     path("delete/<int:pk>/", DeleteCategoryView.as_view()),
#     path("delete/", DeleteCategoryView.as_view()),
#     path("query/", AdvertisementsQueryView.as_view()),
#     path("recomendar/", SaveAdvertisementVoto.as_view()),
#     path("valorados/", AdvertisementMostVoteView.as_view()),
#     path("<int:pk>/change/state/", AdvertisementStateChangeView.as_view()),
# ]


from django.conf.urls import include

from src.application.classified_advertisements.api.views.advertisement.router import Router
from src.application.classified_advertisements.api.views.advertisement.views import (
    AdvertisementViewSet,
)

router = Router()
router.register("", viewset=AdvertisementViewSet, basename="advertisement")
urlpatterns = [path("", include(router.urls))]
