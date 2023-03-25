from django.urls import path
from .views import AdvertisementView,SaveAdvertisementView

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view())
]
