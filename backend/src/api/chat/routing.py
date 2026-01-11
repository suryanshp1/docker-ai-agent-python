from fastapi import APIRouter, Depends, HTTPException
from api.db import get_session
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.ai.services import generate_email_messages
from api.ai.schemas import EmailMessage, SupervisorMessageSchema
from api.ai.agents import get_supervisor
from typing import List

router = APIRouter()

# /api/chat
@router.get("")
def chat_health():
    return {"status": "ok"}


# HTTP POST -> payload = {"message": "hello chat!"} -> {"id": 1, "message": "hello chat!"}
# curl -X POST http://localhost:8080/api/chat -H "Content-Type: application/json" -d '{"message": "hello chat!"}'
# curl -X POST http://localhost:8080/api/chat -H "Content-Type: application/json" -d '{"message": "Tell me how to be a software engineer ?"}'
# curl -X POST http://localhost:8080/api/chat -H "Content-Type: application/json" -d '{"message": "Find how to create a website and send me an email about that"}'
@router.post("", response_model=SupervisorMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
) -> SupervisorMessageSchema:
    # validation
    data = payload.model_dump()

    object_instance = ChatMessage.model_validate(data)

    # ready to store in database
    session.add(object_instance)
    session.commit()
    # session.refresh(object_instance) # ensures id/primary key is added to the object instance

    # generate response
    # response = generate_email_messages(payload.message)

    response = get_supervisor().invoke({"messages": [{"role": "user", "content": payload.message}]})
    if not response:
        raise HTTPException(status_code=400, detail="Failed to generate response")

    messages = response.get("messages", [])
    if not messages:
        raise HTTPException(status_code=400, detail="Failed to generate response")

    message = messages[-1]
    if message.get("role") != "assistant":
        raise HTTPException(status_code=400, detail="Failed to generate response")

    return message

    
# /api/chats/recent/
# curl -X GET http://localhost:8080/api/chat/recent
@router.get("/recent", response_model=List[ChatMessageListItem])
def chat_get_recent_messages(
    session: Session = Depends(get_session)
):
    query = select(ChatMessage).order_by(ChatMessage.id.desc())
    return session.exec(query).fetchall()[:10]

