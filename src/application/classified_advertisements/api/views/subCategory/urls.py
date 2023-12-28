from django.urls import path
from django.conf.urls import include
from src.application.classified_advertisements.api.views.subCategory.router import Router
from src.application.classified_advertisements.api.views.subCategory.view import SubCategoryViewSet

router = Router()
router.register("", viewset=SubCategoryViewSet, basename="sub-categoria")
urlpatterns = [path("", include(router.urls))]
