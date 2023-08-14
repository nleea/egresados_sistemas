import pytest
from django.urls import reverse
from django.test.client import Client
from apps.conftest import user_token

pytestmark = pytest.mark.django_db
reverse_url = reverse("pqrs:asignacion:asignacion-view")


# ----------  Test get ----------- #


def test_asignacion_should_ok(client: Client, user_token):
    response = client.get(
        reverse("pqrs:asignacion:asignacion-view"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    content_json = response.json()
    assert "pqrs" in content_json["data"]
    assert type([]) == type(content_json["data"]["pqrs"])
    assert content_json["data"]["pqrs"] == []


def test_asignacion_solicitudes_should_ok(client: Client, user_token):
    response = client.get(
        reverse("pqrs:asignacion:asignacion-solicitudes"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    content_json = response.json()
    assert type([]) == type(content_json["data"])
    assert content_json["data"] == []
