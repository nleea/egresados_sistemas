import pytest
from apps.conftest import user_token, areas, clear_cache
from django.test.client import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_get_areas_should_ok(client: Client, user_token):
    response = client.get(
        reverse("eventos:areas:areas-list"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )

    assert response.status_code == 200
    response_content = response.json()
    assert response_content["ok"] == True
    assert response_content["data"] == []


@pytest.mark.parametrize(
    "areas",
    [["Exterior", "Interior", "Medio"]],
    indirect=True,
    ids=["areas"],
)
def test_get_areas_list_shouls_ok(client: Client, user_token, areas, clear_cache):
    list_areas = set(map(lambda x: x.name, areas))

    response = client.get(
        reverse("eventos:areas:areas-list"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert len(response_content["data"]) == len(list_areas)
    list_response_areas = set(map(lambda x: x.get("name"), response_content["data"]))
    assert list_response_areas == list_areas


# ------ test POST ------- #


def test_post_create_should_ok(client: Client, user_token):
    response = client.post(
        reverse("eventos:areas:areas-create"),
        data={"name": "Area1"},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["data"] == '"Success"'
    assert response_content["ok"] == True


def test_post_create_should_faild(client: Client, user_token):
    response = client.post(
        reverse("eventos:areas:areas-create"),
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 400
    response_content = response.json()
    assert response_content["errors"] == {"name": ["This field is required."]}
    assert response_content["ok"] == False


@pytest.mark.parametrize("area", ["Area1", "Area2", "Area3"])
def test_post_create_parameters_should_ok(client, user_token, area):
    response = client.post(
        reverse("eventos:areas:areas-create"),
        data={"name": area},
        HTTP_AUTHORIZATION=f"Bearer {user_token}",
    )
    assert response.status_code == 200
    response_content = response.json()
    assert response_content["data"] == '"Success"'
    assert response_content["ok"] == True
