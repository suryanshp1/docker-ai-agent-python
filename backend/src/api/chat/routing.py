from fastapi import APIRouter, Depends
from api.db import get_session
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from typing import List

router = APIRouter()

# /api/chat
@router.get("")
def chat_health():
    return {"status": "ok"}


# HTTP POST -> payload = {"message": "hello chat!"} -> {"id": 1, "message": "hello chat!"}
# curl -X POST http://localhost:8080/api/chat -H "Content-Type: application/json" -d '{"message": "hello chat!"}'
@router.post("")
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    # validation
    data = payload.model_dump()

    object_instance = ChatMessage.model_validate(data)

    # ready to store in database
    session.add(object_instance)
    session.commit()
    session.refresh(object_instance) # ensures id/primary key is added to the object instance

    return object_instance

    
# /api/chats/recent/
# curl -X GET http://localhost:8080/api/chat/recent
@router.get("/recent", response_model=List[ChatMessageListItem])
def chat_get_recent_messages(
    session: Session = Depends(get_session)
):
    query = select(ChatMessage).order_by(ChatMessage.id.desc())
    return session.exec(query).fetchall()[:10]

