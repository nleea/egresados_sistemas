from django.urls import path
from .view import DeleteCapacitacionesView,CapacitacionesView,SaveCapacitacionesView,UpdateCapacitacionesView

urlpatterns = [
    path("",CapacitacionesView.as_view()),
    path("create/",SaveCapacitacionesView.as_view()),
    path("update/<int:pk>/",UpdateCapacitacionesView.as_view()),
    path("delete/<int:pk>/",DeleteCapacitacionesView.as_view())
]
