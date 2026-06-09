from memory.memory_manager import SQLiteMemory

memory = SQLiteMemory()

def get_user_memory(user_id: str):
    return memory.get_conversation_history(user_id)