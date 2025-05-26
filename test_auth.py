from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_missing_token():
    response = client.post("/chat", json={"message": "What is a PE ratio?"})
    assert response.status_code == 422  # Missing auth header

def test_auth_invalid_token():
    response = client.post("/chat", headers={"Authorization": "invalid"}, json={"message": "Test"})
    assert response.status_code == 401
