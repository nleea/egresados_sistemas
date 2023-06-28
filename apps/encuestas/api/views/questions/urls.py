from django.urls import path
from .view import (
    QuestionsView,
    SaveQuestionsView,
    UpdateQuestionsView,
    DeleteQuestionsView,
    SaveQuestionsResponse,
)

urlpatterns = [
    path("", QuestionsView.as_view()),
    path("create/", SaveQuestionsView.as_view()),
    path("update/<int:pk>/", UpdateQuestionsView.as_view()),
    path("delete/<int:pk>/", DeleteQuestionsView.as_view()),
    path("delete/", DeleteQuestionsView.as_view()),
    path("responses/", SaveQuestionsResponse.as_view()),
]
