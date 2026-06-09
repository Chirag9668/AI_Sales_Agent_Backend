from groq import Groq
from tools.catalog_tool import load_catalog

import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class SalesAgent:

    def generate_response(
        self,
        user_message,
        user_memory,
        current_plan=None
    ):

        catalog = load_catalog()

        memory_text = ""

        if user_memory:

            for item in user_memory:

                try:

                    memory_text += (
                        f"{item.role}: "
                        f"{item.message}\n"
                    )

                except Exception:

                    memory_text += (
                        f"{str(item)}\n"
                    )

        else:

            memory_text = (
                "No previous conversation found."
            )

        prompt = f"""
You are a persistent AI sales agent.

CATALOG:
{catalog}

CONVERSATION HISTORY:
{memory_text}

CURRENT ACTIVE PLAN:
{current_plan}

IMPORTANT RULES:

1. CURRENT ACTIVE PLAN is the most recently discussed plan.

2. If the user says:
- that
- it
- this plan

assume they mean CURRENT ACTIVE PLAN.

3. NEVER switch back to an older plan if a newer plan was discussed.

Example:

User: What is your enterprise pricing?
Assistant: Enterprise costs $499/mo.

User: What is your starter pricing?
Assistant: Starter costs $49/mo.

User: Does that include SSO?
Assistant: No. Starter does not include SSO.

4. Answer ONLY the question asked.

5. If user asks pricing:
answer pricing only.

6. If user asks SSO:
answer only about SSO.

7. If user asks features:
answer features only.

8. Do not add extra information.

9. Use ONLY catalog information.

Current User Question:

{user_message}
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                temperature=0.1,
                max_tokens=150
            )

            response_text = (
                response
                .choices[0]
                .message
                .content
            )

        except Exception as e:

            response_text = (
                f"Model Error: {str(e)}"
            )

        return {
            "response": response_text,
            "tools_used": [
                "search_catalog",
                "get_user_memory"
            ]
        }