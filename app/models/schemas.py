from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    query: str
    namespace: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    success: bool
    references: Optional[List[str]] = None

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
