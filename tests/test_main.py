import pytest
from fastapi.testclient import TestClient

client = TestClient()


def test_main(): 
    response = client.get("/")
    assert response.status_code == 200

