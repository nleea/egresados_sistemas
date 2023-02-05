from django.urls import path,include

urlpatterns = [
    path("",include("apps.classified_advertisements.api.views.advertisement.urls")),
    path("seccion/",include("apps.classified_advertisements.api.views.seccion.urls")),
    path("category/",include("apps.classified_advertisements.api.views.category.urls")),
    path("sub/category/",include("apps.classified_advertisements.api.views.subCategory.urls"))
]
