from django.urls import path,re_path
from .view import QuestionsView,SaveQuestionsView,UpdateQuestionsView,DeleteQuestionsView

urlpatterns = [
    re_path(r"(?P<componente>)$",QuestionsView.as_view()),
    path("create/",SaveQuestionsView.as_view()),
    path("update/<int:pk>/",UpdateQuestionsView.as_view()),
    path("delete/<int:pk>/",DeleteQuestionsView.as_view()),
    path("delete/",DeleteQuestionsView.as_view()),
]
