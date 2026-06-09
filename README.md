# Persistent Sales Agent

## Overview

Persistent Sales Agent is an AI-powered sales assistant built using FastAPI, Groq LLM, SQLite, and a persistent memory layer.

The system remembers user conversations across separate API calls and sessions, allowing it to answer follow-up questions using previously discussed context.

Example:

User:
"What is your enterprise pricing?"

Assistant:
"Our Enterprise plan costs $499/mo."

Later:

User:
"Does that include SSO?"

Assistant:
"Yes. The Enterprise plan includes SSO."

The user does not need to repeat the plan name because the agent uses conversation memory and contextual reasoning.

---

## Features

* Persistent conversation memory
* Context-aware follow-up responses
* Product catalog retrieval
* AI-powered response generation using Groq
* Response evaluation layer
* Conversation history management
* REST API using FastAPI
* Swagger API documentation

---

## Architecture

```text
Client
  |
  v
FastAPI API Layer
  |
  v
Chat Service
  |
  +------------------+
  |                  |
  v                  v
Sales Agent      Eval Service
  |
  +------------------+
  |                  |
  v                  v
Catalog Tool    Memory Manager
                    |
                    v
                 SQLite
```

---

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Groq API
* Llama 3.3 70B Versatile
* Pydantic

---

## Project Structure

```text
persistent-sales-agent/

├── agents/
│   └── sales_agent.py

├── api/
│   ├── chat.py
│   └── catalog.py

├── db/
│   └── db_models.py

├── memory/
│   ├── memory_interface.py
│   └── memory_manager.py

├── models/
│   └── schemas.py

├── services/
│   ├── chat_service.py
│   └── eval_service.py

├── tools/
│   ├── catalog_tool.py
│   ├── memory_tool.py
│   └── human_flag_tool.py

├── catalog.json
├── main.py
└── sales_agent.db
```

---

## API Endpoints

### Chat

```http
POST /chat/{user_id}
```

Request:

```json
{
  "message": "What is your enterprise pricing?"
}
```

---

### Conversation History

```http
GET /chat/{user_id}/history
```

---

### Clear Memory

```http
DELETE /chat/{user_id}/memory
```

---

### Catalog

```http
GET /catalog
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Installation

```bash
git clone <repository-url>

cd persistent-sales-agent

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Evaluation Layer

Each response includes:

* Groundedness
* Relevance
* Confidence
* Flagged Status
* Reasoning

These metrics are generated and returned alongside every response.

---

## Future Improvements

* Advanced conversational state tracking
* Human escalation workflow
* Multi-agent architecture
* Vector database memory
* Production deployment enhancements

---

## Security

API keys are not included in the repository and must be provided through environment variables.

---

## Author

Chirag Parmar
