from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_message: str = Field(..., min_length=1, description="User input message to the chatbot")
    conversation_id: Optional[UUID] = Field(None, description="Optional existing conversation ID")


class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the sender (user or assistant)")
    content: str = Field(..., description="Content of the message")
    timestamp: datetime = Field(..., alias="ts", description="Time the message was sent")

    class Config:
        validate_by_name = True


class ChatResponse(BaseModel):
    messages: List[ChatMessage]
    conversation_id: Optional[UUID] = None
