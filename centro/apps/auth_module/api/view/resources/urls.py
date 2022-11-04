from ..modules import path
from .views import  ResourcesListView, ResourcesUpdateView

urlpatterns = [
    path('', ResourcesListView.as_view()),
    path('update/<int:pk>', ResourcesUpdateView.as_view()),
]
