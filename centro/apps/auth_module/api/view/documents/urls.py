from ..modules import path
from .views import DocumentListView, DocumentUpdateView, DocumentCreateView, DocumentDestroyView

urlpatterns = [
    path('', DocumentListView.as_view()),
    path('update/<int:pk>', DocumentUpdateView.as_view()),
    path('create/', DocumentCreateView.as_view()),
    path('delete/<int:pk>', DocumentDestroyView.as_view()),
    
]
