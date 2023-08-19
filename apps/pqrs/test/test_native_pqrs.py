import pytest
from django.test.client import Client
from django.urls import reverse
from apps.conftest import user_token, create_pqrs
from apps.pqrs.models.models import Pqrs

pytestmark = pytest.mark.django_db


def test_pqrs_should_ok(client: Client, user_token):
    response = client.get(
        reverse("pqrs:pqrs_module:list-pqrs"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert len(response_content["data"]) == 0
    assert response_content["ok"] == True


def test_one_pqrs_should_ok(client: Client, user_token):
    response = client.get(
        reverse("pqrs:pqrs_module:list-pqrs"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["ok"] == True
    # assert response_content["data"][0]["id"] == create_pqrs.pk


# ----------- Test POST --------------- #
def test_create_pqrs_should_ok(client: Client, user_token, create_tipo):
    response = client.post(
        reverse("pqrs:pqrs_module:create-pqrs"),
        data={
            "description": "description",
            "persona": 1,
            "tipopqrs": create_tipo.pk,
            "titulo": "titulo",
        },
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    response_content = response.json()
    assert response.status_code == 200
    assert response_content["data"] == '"Sucess"'
    assert response_content["ok"] == True


def test_create_pqrs_should_faild(client: Client, user_token):
    response = client.post(
        reverse("pqrs:pqrs_module:create-pqrs"),
        data={
            "description": "description",
            "persona": 1,
            "titulo": "titulo",
        },
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    response_content = response.json()
    assert response.status_code == 400
    assert response_content["errors"] == {"tipopqrs": ["This field is required."]}
    assert response_content["ok"] == False


def test_create_pqrs_should_faild_title(client: Client, user_token, create_tipo):
    response = client.post(
        reverse("pqrs:pqrs_module:create-pqrs"),
        data={
            "description": "description",
            "persona": 1,
            "tipopqrs": create_tipo.pk,
        },
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    response_content = response.json()
    assert response.status_code == 400
    assert response_content["errors"] == {"titulo": ["This field is required."]}
    assert response_content["ok"] == False


def test_create_pqrs_should_faild_description(client: Client, user_token, create_tipo):
    response = client.post(
        reverse("pqrs:pqrs_module:create-pqrs"),
        data={
            "persona": 1,
            "tipopqrs": create_tipo.pk,
            "titulo": "titulo",
        },
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    response_content = response.json()
    assert response.status_code == 400
    assert response_content["errors"] == {"description": ["This field is required."]}
    assert response_content["ok"] == False
    
def test_create_pqrs_should_faild_empty(client: Client, user_token, create_tipo):
    response = client.post(
        reverse("pqrs:pqrs_module:create-pqrs"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    response_content = response.json()
    assert response.status_code == 400
    assert response_content["ok"] == False
