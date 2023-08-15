import pytest
from django.urls import reverse
from django.test.client import Client
from apps.conftest import user_token, create_pqrs, create_pqrs_list
from apps.pqrs.models.models import Pqrs, TipoPqrs

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


def test_asignacion_solicitudes_list_should_ok(client: Client, user_token, create_pqrs):
    response = client.get(
        reverse("pqrs:asignacion:asignacion-solicitudes"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["data"][0]["id"] == create_pqrs.pk
    assert response_content["data"][0]["titulo"] == create_pqrs.titulo
    assert response_content["data"][0]["description"] == create_pqrs.description


@pytest.mark.parametrize(
    "create_pqrs_list",
    [
        [
            ("description", 1, "titulo"),
            ("description2", 1, "titulo2"),
            ("description3", 1, "titulo3"),
            ("description4", 1, "titulo4"),
        ]
    ],
    indirect=True,
)
def test_asignacion_solicitudes_list_parameters_should_ok(
    client: Client, user_token, create_pqrs_list
):
    pqrs_description = set(map(lambda x: x.description, create_pqrs_list))
    response = client.get(
        reverse("pqrs:asignacion:asignacion-solicitudes"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 200
    response_content = response.json()
    assert len(response_content["data"]) == len(create_pqrs_list)
    assert pqrs_description == set(map(lambda x: x.get("description"), response_content["data"]))


# ----------  Test POST ----------- #


def test_asignacion_solicitudes_should_fail_post(client: Client, user_token):
    response = client.post(
        reverse("pqrs:asignacion:asignacion-create"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 400
    response_content = response.json()

    assert response_content["errors"]["pqrs"] == ["This field is required."]
    assert response_content["ok"] == False


@pytest.mark.parametrize(
    "tipo,persona,", [("Reclamo", 1), ("Peticion", 2), ("Queja", 1)]
)
def test_asignacion_solicitudes_should_ok_post(
    client: Client, user_token, tipo, persona
):
    pk = TipoPqrs.objects.create(tipo=tipo).pk
    Pqrs.objects.create(
        description="description", persona_id=persona, tipopqrs_id=pk, titulo="titulo"
    )
    response = client.post(
        reverse("pqrs:asignacion:asignacion-create"),
        data={"pqrs": 1},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 200
    response_content = response.json()

    assert response_content["data"] == '"Sucess"'
