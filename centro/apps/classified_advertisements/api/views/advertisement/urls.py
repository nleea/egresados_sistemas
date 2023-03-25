from django.urls import path
<<<<<<< HEAD
from .views import AdvertisementView,SaveAdvertisementView

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view())
=======
from .views import AdvertisementView,SaveAdvertisementView,DeleteAnuncioView,UpdateAnuncioView,ListaAll

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view()),
    path("delete/<int:pk>",DeleteAnuncioView.as_view()),
    path("update/<int:pk>",UpdateAnuncioView.as_view()),
    path("all/",ListaAll.as_view())
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345
]
