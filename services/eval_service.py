from groq import Groq
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class EvalService:

    def evaluate(
        self,
        user_question,
        response,
        tools_used
    ):

        prompt = f"""
You are an AI evaluator.

User Question:
{user_question}

Agent Response:
{response}

Tools Used:
{tools_used}

Return ONLY valid JSON.

Schema:

{{
    "groundedness": float,
    "relevance": float,
    "confidence": float,
    "flagged": boolean,
    "reasoning": string
}}

Scoring Guidelines:

groundedness:
0.0-1.0

relevance:
0.0-1.0

confidence:
0.0-1.0

flagged:
true if response appears unsupported,
hallucinated,
or low quality.
"""

        try:

            result = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a response evaluator."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )

            eval_text = (
                result
                .choices[0]
                .message
                .content
            )

            start = eval_text.find("{")
            end = eval_text.rfind("}") + 1

            eval_json = json.loads(
                eval_text[start:end]
            )

            return eval_json

        except Exception as e:

            return {
                "groundedness": 0.5,
                "relevance": 0.5,
                "confidence": 0.5,
                "flagged": True,
                "reasoning":
                    f"Evaluation failed: {str(e)}"
            }