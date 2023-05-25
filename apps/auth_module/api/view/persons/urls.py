from ..modules import path
from .persons import PersonCreateView, PersonView, PersonUpdateView, CreateAPIView

urlpatterns = [
    path('', PersonView.as_view()),
    path('update/profile/', PersonUpdateView.as_view()),
    path('create/', PersonCreateView.as_view())
]
