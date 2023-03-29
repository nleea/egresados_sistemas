from django.urls import path
from .users import UsersView, UserCreateView, UserUpdateView, UsersViewPublic, UserChangePasswordView

urlpatterns = [
    path('', UsersView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('public/', UsersViewPublic.as_view()),
    path('<int:pk>/change/password/', UserChangePasswordView.as_view())
]
