from ..modules import path
from .views import GenderCreateView, GenderListView, GenderUpdateView

urlpatterns = [
    path('', GenderListView.as_view()),
    path('update/<int:pk>', GenderUpdateView.as_view()),
    path('create/', GenderCreateView.as_view())
]
