from services.eval_service import EvalService
from agents.sales_agent import SalesAgent
from memory.memory_manager import SQLiteMemory

import uuid


class ChatService:

    def __init__(self):

        self.agent = SalesAgent()
        self.memory = SQLiteMemory()
        self.eval_service = EvalService()

    def process_message(
        self,
        user_id: str,
        user_message: str
    ):

        # Read memory
        user_memory = self.memory.get_conversation_history(
            user_id
        )

        # Detect active plan
        current_plan = None

        message_lower = user_message.lower()

        if "starter" in message_lower:
            current_plan = "Starter"

        elif "growth" in message_lower:
            current_plan = "Growth"

        elif "enterprise" in message_lower:
            current_plan = "Enterprise"

        else:

            for item in reversed(user_memory):

                text = item.message.lower()

                if "starter" in text:
                    current_plan = "Starter"
                    break

                elif "growth" in text:
                    current_plan = "Growth"
                    break

                elif "enterprise" in text:
                    current_plan = "Enterprise"
                    break

        # Generate response
        agent_response = self.agent.generate_response(
            user_message=user_message,
            user_memory=user_memory,
            current_plan=current_plan
        )

        response_text = agent_response["response"]

        # Save user message
        self.memory.save_conversation(
            user_id=user_id,
            role="user",
            message=user_message
        )

        # Save assistant response
        self.memory.save_conversation(
            user_id=user_id,
            role="assistant",
            message=response_text
        )

        # Evaluation
        eval_result = self.eval_service.evaluate(
            user_message,
            response_text,
            agent_response["tools_used"]
        )

        return {
            "response": response_text,
            "eval": eval_result,
            "tools_used": agent_response["tools_used"],
            "session_id": str(uuid.uuid4())
        }

    def get_history(
        self,
        user_id: str
    ):

        return self.memory.get_conversation_history(
            user_id
        )

    def clear_memory(
        self,
        user_id: str
    ):

        self.memory.clear_conversation_history(
            user_id
        )