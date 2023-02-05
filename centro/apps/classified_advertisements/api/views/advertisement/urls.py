from django.urls import path
<<<<<<< HEAD
from .views import AdvertisementView,SaveAdvertisementView

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view())
=======
from .views import AdvertisementView

urlpatterns = [
    path("",AdvertisementView.as_view())
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
]
