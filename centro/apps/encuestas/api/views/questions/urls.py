from django.urls import path
from .view import QuestionsView,SaveQuestionsView,UpdateQuestionsView

urlpatterns = [
    path("",QuestionsView.as_view()),
    path("create/",SaveQuestionsView.as_view()),
    path("update/<int:pk>/",UpdateQuestionsView.as_view())
]
