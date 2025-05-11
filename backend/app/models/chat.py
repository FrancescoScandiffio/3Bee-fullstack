import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy import Uuid
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Conversation(Base):
    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(Uuid(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=True)

    # one to many -> ConversationMessage
    messages = relationship('ConversationMessage', back_populates='conversation', cascade="all, delete-orphan")


class ConversationMessage(Base):
    __tablename__ = 'conversation_messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'), nullable=False)
    content = Column(String, nullable=False)
    time = Column(DateTime(timezone=True), nullable=False, default=func.now())
    role = Column(String, nullable=False)

    # many to one -> Conversation
    conversation = relationship('Conversation', back_populates='messages')
