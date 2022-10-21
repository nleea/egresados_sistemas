from django.urls import path

from .view import AuthLogin, AuthRegister

urlpatterns = [
    path('login/', AuthLogin.as_view()),
    path('register/', AuthRegister.as_view())
]
