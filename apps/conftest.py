import pytest
from django.test.client import Client
from rest_framework_simplejwt.tokens import RefreshToken

username = "admin"
password = "12345678"

@pytest.fixture
def user_token(client,django_user_model):
    client.login(username=username, password=password)
    user = django_user_model.objects.get(username=username)
    refresh = RefreshToken.for_user(user=user)
    return str(refresh.access_token)