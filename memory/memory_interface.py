from abc import ABC, abstractmethod

class AbstractMemory(ABC):
    @abstractmethod
    def save_conversation(self, user_id: str, role: str, message: str):
        pass

    @abstractmethod
    def get_conversation_history(self, user_id: str):
        pass
    
    @abstractmethod
    def clear_conversation_history(self, user_id: str):
        pass