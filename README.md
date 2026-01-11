# Deploy AI Agent

This project is a deployed AI agent application built with a modern Python stack, designed to be containerized and scalable. It features a FastAPI backend, LangChain for AI orchestration, and a PostgreSQL database.

## 🚀 Technology Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) - High performance, easy to learn, fast to code, ready for production.
- **AI Orchestration**: [LangChain](https://www.langchain.com/) & [LangGraph](https://langchain-ai.github.io/langgraph/) - Building applications with LLMs through composability.
- **Database**: [PostgreSQL](https://www.postgresql.org/) (via [SQLModel](https://sqlmodel.tiangolo.com/)) - The World's Most Advanced Open Source Relational Database.
- **Containerization**: [Docker](https://www.docker.com/) & Docker Compose - Simplify deployment and development.
- **Server**: [Uvicorn](https://www.uvicorn.org/) - An ASGI web server implementation for Python.

## 📋 Prerequisites

Ensure you have the following installed on your machine:

- **Docker Desktop**: [Download and Install](https://www.docker.com/products/docker-desktop)
- **Git**: [Download and Install](https://git-scm.com/downloads)

## 🛠️ Setup & Installation

1.  **Clone the repository**

    ```bash
    git clone <repository-url>
    cd deploy-ai-agent
    ```

2.  **Configure Environment Variables**

    Copy the sample environment file to `.env`:

    ```bash
    cp .env.sample .env
    ```

    Open `.env` and fill in the necessary keys (e.g., `OPENAI_API_KEY` or other LLM provider keys if required by `src/api/ai/agents.py`).

3.  **Run with Docker Compose**

    Build and start the services:

    ```bash
    docker compose up --build
    ```

    The application will be available at `http://localhost:8080` (mapped from container port 8000).

## 📂 Project Structure

```text
.
├── backend/            # Backend source code
│   ├── src/
│   │   ├── api/        # API endpoints and logic
│   │   │   ├── ai/     # AI agents and schemas
│   │   │   └── chat/   # Chat routing
│   │   └── main.py     # Application entry point
│   ├── Dockerfile
│   └── requirements.txt
├── compose.yaml        # Docker Compose service definition
├── static_html/        # Static frontend assets (if enabled)
└── README.md           # Project documentation
```

## 🔌 API Endpoints

Once the server is running, you can access the interactive API documentation (Swagger UI) at:

- **URL**: `http://localhost:8080/docs`

Test the chat endpoint:

```bash
curl -X POST http://localhost:8080/api/chat \
-H "Content-Type: application/json" \
-d '{"message": "Hello, AI!"}'
```
