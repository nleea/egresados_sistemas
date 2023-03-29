from django.urls import path
from .views import AdvertisementView,SaveAdvertisementView,DeleteCategoryView,UpdateCategoryView

urlpatterns = [
    path("",AdvertisementView.as_view()),
    path("create/",SaveAdvertisementView.as_view()),
    path("update/<int:pk>/",UpdateCategoryView.as_view()),
    path("delete/<int:pk>/",DeleteCategoryView.as_view())
]
