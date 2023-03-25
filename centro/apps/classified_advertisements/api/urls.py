from django.urls import path,include

urlpatterns = [
    path("",include("apps.classified_advertisements.api.views.advertisement.urls")),
<<<<<<< HEAD
=======
    path("seccion/",include("apps.classified_advertisements.api.views.seccion.urls")),
>>>>>>> d88e9d6c7916f48e9ff67d1f9c4c6efd47899345
    path("category/",include("apps.classified_advertisements.api.views.category.urls")),
    path("sub/category/",include("apps.classified_advertisements.api.views.subCategory.urls"))
]
