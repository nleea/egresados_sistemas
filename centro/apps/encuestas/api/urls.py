from django.urls import path,include

urlpatterns = [
    path("questions/",include("apps.encuestas.api.views.questions.urls")),
    path("momentos/",include("apps.encuestas.api.views.moments.urls")),
    
]
