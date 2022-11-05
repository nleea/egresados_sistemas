from ..modules import path
from .views import  ResourcesListView, ResourcesUpdateView

urlpatterns = [
    path('roles/', ResourcesListView.as_view()),
    path('update/<int:pk>', ResourcesUpdateView.as_view()),
]
