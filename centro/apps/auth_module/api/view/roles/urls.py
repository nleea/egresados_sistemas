from ..modules import path
from .views import RolescreateView, RolesListView, RoleUpdateView

urlpatterns = [
    path('', RolesListView.as_view()),
    path('update/<int:pk>', RoleUpdateView.as_view()),
    path('create/', RolescreateView.as_view())
]
