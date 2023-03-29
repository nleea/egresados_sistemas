from django.urls import path,include

urlpatterns = [
    path("",include("apps.classified_advertisements.api.views.advertisement.urls")),
    path("category/",include("apps.classified_advertisements.api.views.category.urls")),
    path("sub/category/",include("apps.classified_advertisements.api.views.subCategory.urls")),
    path("capacitaciones/",include("apps.classified_advertisements.api.views.capacitaciones.urls")),
    path("producto/",include("apps.classified_advertisements.api.views.producto.urls"))
    
]
