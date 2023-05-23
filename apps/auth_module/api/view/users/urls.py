from django.urls import path,re_path
from .users import UsersView, UserCreateView, UserUpdateView, UsersViewPublic, UserChangePasswordView

urlpatterns = [
    re_path(r'(?P<all>)$', UsersView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('public/', UsersViewPublic.as_view()),
    path('<int:pk>/change/password/', UserChangePasswordView.as_view())
]
