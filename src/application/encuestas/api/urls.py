from django.urls import path, include
from src.application.constants import PATH_APP

urlpatterns = [
    path("questions/", include(f"{PATH_APP}.encuestas.api.views.questions.urls")),
    path("momentos/", include(f"{PATH_APP}.encuestas.api.views.moments.urls")),
]
