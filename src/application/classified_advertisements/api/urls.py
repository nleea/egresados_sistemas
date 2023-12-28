from django.urls import path,include
from src.application.constants import PATH_APP

urlpatterns = [
    path("",include(f"{PATH_APP}.classified_advertisements.api.views.advertisement.urls")),
    path("category/",include(f"{PATH_APP}.classified_advertisements.api.views.category.urls")),
    path("sub/category/",include(f"{PATH_APP}.classified_advertisements.api.views.subCategory.urls")),
    path("capacitaciones/",include(f"{PATH_APP}.classified_advertisements.api.views.capacitaciones.urls")), 
]
