from django.urls import path,include

urlpatterns = [
<<<<<<< HEAD
    path("",include("apps.classified_advertisements.api.views.advertisement.urls")),
    path("seccion/",include("apps.classified_advertisements.api.views.seccion.urls")),
    path("category/",include("apps.classified_advertisements.api.views.category.urls")),
    path("sub/category/",include("apps.classified_advertisements.api.views.subCategory.urls"))
=======
    path("",include("apps.classified_advertisements.api.views.advertisement.urls"))
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
]
