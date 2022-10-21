from ..modules import path
from .views import ResourcesCreateView, ResourcesListView, ResourcesUpdateView

urlpatterns = [
    path('', ResourcesListView.as_view()),
    path('update/<int:pk>', ResourcesUpdateView.as_view()),
    path('create/', ResourcesCreateView.as_view())
]
