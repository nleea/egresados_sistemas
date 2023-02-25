from django.urls import path
from .views import AdvertisementView,SaveAdvertisementView,DeleteAnuncioView,UpdateAnuncioView,ListaAll

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view()),
    path("delete/<int:pk>",DeleteAnuncioView.as_view()),
    path("update/<int:pk>",UpdateAnuncioView.as_view()),
    path("all/",ListaAll.as_view())
]
