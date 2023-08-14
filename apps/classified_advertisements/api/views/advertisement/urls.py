from django.urls import path, re_path
from .views import (
    AdvertisementView,
    SaveAdvertisementView,
    DeleteCategoryView,
    UpdateCategoryView,
    AdvertisementsQueryView,
    MyAdvertisementView,
    SaveAdvertisementVoto,
    AdvertisementMostVoteView,
    AdvertisementStateView,
    AdvertisementStateChangeView
)

urlpatterns = [
    re_path(r"(?P<subCategoryId>\w{0,50})$", AdvertisementView.as_view()),
    path("mine/", MyAdvertisementView.as_view()),
    path("create/", SaveAdvertisementView.as_view()),
    path("update/<int:pk>/", UpdateCategoryView.as_view()),
    path("delete/<int:pk>/", DeleteCategoryView.as_view()),
    path("delete/", DeleteCategoryView.as_view()),
    path("query/", AdvertisementsQueryView.as_view()),
    path("recomendar/", SaveAdvertisementVoto.as_view()),
    path("valorados/", AdvertisementMostVoteView.as_view()),
    path("state/", AdvertisementStateView.as_view()),
    path("<int:pk>/change/state/",AdvertisementStateChangeView.as_view())
]
