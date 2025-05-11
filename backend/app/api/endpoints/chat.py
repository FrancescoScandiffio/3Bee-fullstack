from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter

from app.schemas.chat import ChatResponse, ChatRequest, ChatMessage

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    mocked_messages = [
        ChatMessage(role="user", content=request.user_message, ts=datetime.now(timezone.utc)
                    ),
        ChatMessage(role="assistant", content="This is a mock response.", ts=datetime.now(timezone.utc)
                    ),
    ]

    response = ChatResponse(
        messages=mocked_messages,
        conversation_id=request.conversation_id or uuid4()
    )
    return response
