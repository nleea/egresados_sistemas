from ..modules import path
from .views import  ResourcesListView, ResourcesUpdateView,ResourcesDestroyView

urlpatterns = [
    path('roles/', ResourcesListView.as_view()),
    path('update/<int:pk>', ResourcesUpdateView.as_view()),
    path('delete/<int:pk>', ResourcesDestroyView.as_view()),
]
