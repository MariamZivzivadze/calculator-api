"""
Tests for the Calculator API.

This shows the pytest + Flask test client pattern (Module 7):
- `client` fixture spins up a fake in-memory client, no real server needed
- each test hits a route and checks status code + JSON response
"""

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "endpoints" in response.get_json()


def test_add(client):
    response = client.post("/add", json={"a": 4, "b": 5})
    assert response.status_code == 200
    assert response.get_json()["result"] == 9


def test_subtract(client):
    response = client.post("/subtract", json={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.get_json()["result"] == 7


def test_multiply(client):
    response = client.post("/multiply", json={"a": 6, "b": 7})
    assert response.status_code == 200
    assert response.get_json()["result"] == 42


def test_divide(client):
    response = client.post("/divide", json={"a": 20, "b": 4})
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_divide_by_zero(client):
    response = client.post("/divide", json={"a": 5, "b": 0})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_missing_operand(client):
    response = client.post("/add", json={"a": 5})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_non_numeric_input(client):
    response = client.post("/add", json={"a": "hello", "b": 5})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_no_json_body(client):
    response = client.post("/add")
    assert response.status_code == 400
