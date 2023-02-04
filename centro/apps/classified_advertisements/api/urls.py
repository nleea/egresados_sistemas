from django.urls import path,include

urlpatterns = [
    path("",include("apps.classified_advertisements.api.views.advertisement.urls"))
]
