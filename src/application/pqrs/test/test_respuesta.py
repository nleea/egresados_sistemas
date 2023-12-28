import pytest
from src.conftest import user_token, respuesta_create
from django.urls import reverse
from django.test.client import Client

pytestmark = pytest.mark.django_db


# -------- Test GET -------- #


def test_respuesta_should_ok(client: Client, user_token):
    response = client.get(
        reverse("pqrs:respuesta:respuesta-list"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["ok"] == True
    assert response_content["data"] == []


def test_respuesta_valid_should_ok(client: Client, user_token, respuesta_create):
    response = client.get(
        reverse("pqrs:respuesta:respuesta-list"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["ok"] == True
    assert response_content["data"][0].get("pqrs") == respuesta_create


# -------- Test POST -------- #


def test_respuesta_post_should_ok(client: Client, user_token, create_pqrs):
    respuesta = client.post(
        reverse("pqrs:respuesta:respuesta-create"),
        data={"pqrs": create_pqrs.pk, "descripcion": "descripcion"},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert respuesta.status_code == 200
    respuesta_content = respuesta.json()
    assert respuesta_content["data"] == '"Sucess"'
    assert respuesta_content["ok"] == True


def test_respuesta_post_should_faild(client: Client, user_token, create_pqrs):
    respuesta = client.post(
        reverse("pqrs:respuesta:respuesta-create"),
        data={"pqrs": create_pqrs.pk},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert respuesta.status_code == 400
    respuesta_content = respuesta.json()
    assert respuesta_content["errors"] == {"descripcion": ["This field is required."]}
    assert respuesta_content["ok"] == False


def test_respuesta_post_without_pqrs_should_faild(
    client: Client, user_token, create_pqrs
):
    respuesta = client.post(
        reverse("pqrs:respuesta:respuesta-create"),
        data={"descripcion": "descripcion"},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert respuesta.status_code == 400
    respuesta_content = respuesta.json()
    assert respuesta_content["errors"] == {"pqrs": ["This field is required."]}
    assert respuesta_content["ok"] == False
