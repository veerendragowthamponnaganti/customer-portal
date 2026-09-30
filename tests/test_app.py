import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app.app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_register_customer():
    client = app.test_client()

    response = client.post(
        "/customers",
        json={
            "name": "Rahul",
            "email": "rahul@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json["name"] == "Rahul"
    assert response.json["email"] == "rahul@example.com"


def test_get_customers():
    client = app.test_client()

    response = client.get("/customers")

    assert response.status_code == 200
    assert isinstance(response.json, list)