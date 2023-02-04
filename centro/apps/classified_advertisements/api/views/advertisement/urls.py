from django.urls import path
from .views import AdvertisementView

urlpatterns = [
    path("",AdvertisementView.as_view())
]
