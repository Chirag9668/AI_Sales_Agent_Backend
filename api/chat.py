from fastapi import APIRouter
from models.schemas import Message
from services.chat_service import ChatService

from memory.memory_manager import SQLiteMemory

router = APIRouter()

chat_service = ChatService()

memory = SQLiteMemory()


@router.post("/chat/{user_id}")
def chat(
    user_id: str,
    request: Message
):

    return chat_service.process_message(
        user_id,
        request.message
    )


@router.get("/chat/{user_id}/history")
def get_conversation_history(
    user_id: str
):

    history = memory.get_conversation_history(user_id)

    return [
        {
            "role": item.role,
            "message": item.message
        }
        for item in history
    ]


@router.delete("/chat/{user_id}/memory")
def clear_conversation_history(
    user_id: str
):

    memory.clear_conversation_history(user_id)

    return {
        "message":
            f"Conversation history cleared for {user_id}"
    }