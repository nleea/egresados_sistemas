# from django.urls import path
# from .views import DeleteEventosSubAreaView, SaveEventosSubAreaView, UpdateEventosSubAreaView, EventosSubAreaView, EventosQuery

# urlpatterns = [
#     path("", EventosSubAreaView.as_view()),
#     path("create/", SaveEventosSubAreaView.as_view()),
#     path("update/<int:pk>/", UpdateEventosSubAreaView.as_view()),
#     path("delete/<int:pk>/", DeleteEventosSubAreaView.as_view()),
#     path("delete/", DeleteEventosSubAreaView.as_view()),
#     path("query/", EventosQuery.as_view())
# ]

from django.urls import path
from django.conf.urls import include
from src.application.eventos.api.views.subAreas.router import Router
from src.application.eventos.api.views.subAreas.views import SubAreaViewSet

router = Router()
router.register("", viewset=SubAreaViewSet, basename="sub_area")
urlpatterns = [path("", include(router.urls))]
