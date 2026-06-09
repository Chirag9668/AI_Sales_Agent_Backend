from db.database import SessionLocal
from db.db_models import Conversation
from memory.memory_interface import AbstractMemory

class SQLiteMemory(AbstractMemory):
    #save conversation to the database
    def save_conversation(self, user_id: str, role: str, message: str):
        db = SessionLocal()
        conversation = Conversation(
            user_id=user_id,
            role=role,
            message=message
        )
        db.add(conversation)
        db.commit()
        db.close()
        
    #retrieve conversation history for a user    
    def get_conversation_history(self, user_id: str):
        db = SessionLocal()
        conversations = (
            db.query(Conversation).filter(Conversation.user_id == user_id).all()
            )
        db.close()
        return conversations
    
    #clear conversation history for a user
    def clear_conversation_history(self, user_id: str):
        db = SessionLocal()
        db.query(Conversation).filter(Conversation.user_id == user_id).delete()
        db.commit()
        db.close()