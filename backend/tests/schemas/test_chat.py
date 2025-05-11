from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from app.schemas.chat import ChatRequest, ChatMessage, ChatResponse


def test_chat_request_valid():
    req = ChatRequest(user_message="Hello", conversation_id=uuid4())
    assert req.user_message == "Hello"
    assert isinstance(req.conversation_id, type(uuid4()))


def test_chat_request_missing_conversation_id():
    req = ChatRequest(user_message="Hello")
    assert req.conversation_id is None


def test_chat_request_invalid_empty_message():
    with pytest.raises(ValidationError):
        ChatRequest(user_message="")


def test_chat_message_valid():
    now = datetime.now(timezone.utc)
    msg = ChatMessage(role="user", content="Hi", ts=now)
    assert msg.role == "user"
    assert msg.content == "Hi"
    assert msg.timestamp == now


def test_chat_response_with_conversation_id():
    now = datetime.now(timezone.utc)
    resp = ChatResponse(
        conversation_id=uuid4(),
        messages=[
            ChatMessage(role="user", content="Hi", ts=now),
            ChatMessage(role="assistant", content="Hello!", ts=now),
        ],
    )
    assert len(resp.messages) == 2
    assert resp.conversation_id is not None


def test_chat_response_without_conversation_id():
    now = datetime.now(timezone.utc)
    resp = ChatResponse(
        messages=[ChatMessage(role="user", content="Test", ts=now)]
    )
    assert resp.conversation_id is None
