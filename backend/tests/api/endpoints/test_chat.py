from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint_with_conversation_id():
    response = client.post("/chat", json={
        "user_message": "Hello there!",
        "conversation_id": str(uuid4())
    })

    assert response.status_code == 200
    data = response.json()
    assert "messages" in data
    assert isinstance(data["messages"], list)
    assert all(k in data["messages"][0] for k in ("role", "content", "ts"))
    assert "conversation_id" in data


def test_chat_endpoint_without_conversation_id():
    response = client.post("/chat", json={"user_message": "Start new"})
    assert response.status_code == 200
    data = response.json()
    assert data["conversation_id"] is not None
    assert len(data["messages"]) == 2


def test_chat_endpoint_invalid_input():
    response = client.post("/chat", json={"user_message": ""})
    assert response.status_code == 422
