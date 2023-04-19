from django.urls import path
from .views import DeleteTipoEventosView,SaveTipoEventos,UpdateTipoEventosView,TipoEventosView

urlpatterns = [
    path("", TipoEventosView.as_view()),
    path("create/", SaveTipoEventos.as_view()),
    path("update/<int:pk>/", UpdateTipoEventosView.as_view()),
    path("delete/<int:pk>/", DeleteTipoEventosView.as_view())
]
