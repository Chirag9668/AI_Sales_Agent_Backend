from pydantic import BaseModel

class Message(BaseModel):
    message: str
    
class EvalResponse(BaseModel):
    groundedness: float
    relevance: float
    confidence: float
    flagged: bool
    reasoning: str
    
class ChatResponse(BaseModel):
    response: str
    eval: EvalResponse
    tools_used: list[str]
    session_id: str    