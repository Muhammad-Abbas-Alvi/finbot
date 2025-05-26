from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post(
        "/chat",
        headers={"Authorization": "finance123"},
        json={"message": "What is the meaning of PE ratio?"}
    )
    assert response.status_code == 200
    assert "reply" in response.json()
