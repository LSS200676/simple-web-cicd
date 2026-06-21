""" Flask App Unit Tests v2.0 """
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_index_contains_ci_cd_keyword(client):
    rv = client.get("/")
    assert b"CI/CD" in rv.data


def test_index_contains_student_info(client):
    rv = client.get("/")
    data = rv.data.decode("utf-8")
    assert "2440666125" in data
    assert "赖石生" in data


def test_health_check_endpoint(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.get_json()["status"] == "healthy"


def test_api_info_endpoint_v2(client):
    rv = client.get("/api/info")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["version"] == "2.0"
    assert data["student_id"] == "2440666125"
    assert data["student_name"] == "赖石生"
