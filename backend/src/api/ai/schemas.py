from pydantic import BaseModel, Field


class EmailMessage(BaseModel):
    subject: str
    content: str
    invalid_request: bool | None = Field(default=False)