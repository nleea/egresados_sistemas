from django.urls import path

from .view import AuthLogin, AuthRegister, LogoutView

urlpatterns = [
    path('login/', AuthLogin.as_view()),
    path('register/', AuthRegister.as_view()),
    path('logout/', LogoutView.as_view())
]
