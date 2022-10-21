from ..modules import path
from .views import DocumentListView, DocumentUpdateView, DocumentCreateView

urlpatterns = [
    path('', DocumentListView.as_view()),
    path('update/<int:pk>', DocumentUpdateView.as_view()),
    path('create/', DocumentCreateView.as_view())
]
