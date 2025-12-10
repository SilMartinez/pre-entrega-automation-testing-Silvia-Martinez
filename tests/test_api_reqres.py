import pytest
import requests
from faker import Faker

from utils.data_loader import load_json

fake = Faker()
BASE_API = "https://reqres.in/api"


@pytest.mark.api
def test_get_users_devuelve_200_y_lista():

    resp = requests.get(f"{BASE_API}/users?page=2")
    assert resp.status_code == 200

    body = resp.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@pytest.mark.api
def test_post_create_user_con_faker():

    payload = {"name": fake.name(), "job": fake.job()}

    resp = requests.post(f"{BASE_API}/users", json=payload)
    assert resp.status_code == 201

    data = resp.json()
    assert data["name"] == payload["name"]
    assert "id" in data
    assert "createdAt" in data


@pytest.mark.api
@pytest.mark.parametrize("key", ["nuevo_usuario", "otro_usuario"])
def test_post_create_user_desde_json(key):

    payloads = load_json("api_payloads.json")
    payload = payloads[key]

    resp = requests.post(f"{BASE_API}/users", json=payload)
    assert resp.status_code == 201


@pytest.mark.api
def test_put_update_user():

    payload = {"name": "User Put", "job": "QA Senior"}

    resp = requests.put(f"{BASE_API}/users/2", json=payload)
    assert resp.status_code == 200

    data = resp.json()
    assert data["name"] == payload["name"]
    assert "updatedAt" in data


@pytest.mark.api
def test_patch_update_user():

    payload = {"job": "Automation Lead"}

    resp = requests.patch(f"{BASE_API}/users/2", json=payload)
    assert resp.status_code == 200

    data = resp.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data


@pytest.mark.api
def test_delete_user():

    resp = requests.delete(f"{BASE_API}/users/2")
    assert resp.status_code == 204