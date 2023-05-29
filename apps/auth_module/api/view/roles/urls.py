from ..modules import path
from .views import RolescreateView, RolesListView

urlpatterns = [
    path('', RolesListView.as_view()),
    # path('update/<int:pk>', RoleUpdateView.as_view()),
    path('create/', RolescreateView.as_view()),
    # path('delete/<int:pk>', RolesDestroyView.as_view()),
]
