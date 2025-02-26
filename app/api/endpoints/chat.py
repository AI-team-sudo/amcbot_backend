from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import ChatRequest, ChatResponse, ErrorResponse
from app.services.chat_service import ChatService
from app.core.security import verify_api_key

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post(
    "/query",
    response_model=ChatResponse,
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}}
)
async def chat_query(
    request: ChatRequest,
    chat_service: ChatService = Depends(),
    _: bool = Depends(verify_api_key)
):
    try:
        response, success, references = await chat_service.process_query(
            request.query,
            request.namespace
        )

        return ChatResponse(
            response=response,
            success=success,
            references=references
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
