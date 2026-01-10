from sqlmodel import SQLModel, Field, DateTime
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo

def get_utc_now():
    return datetime.now(ZoneInfo("UTC"))

class ChatMessagePayload(SQLModel):
    # pydantic model
    # validation
    # serializer
    message: str

class ChatMessage(SQLModel, table=True):
    # database table
    # saving, updating, getting, deleting
    # serializer
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(default=get_utc_now(), 
        sa_type=DateTime(timezone=True), 
        primary_key=False,
        nullable=False,
    )

class ChatMessageListItem(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)