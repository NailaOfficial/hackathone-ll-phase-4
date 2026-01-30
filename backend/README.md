# Task Management API - Backend Service

A robust RESTful API built with FastAPI, featuring intelligent task management through AI-powered conversational interfaces and traditional CRUD operations.

## Technology Foundation

- **Web Framework:** FastAPI 0.125+
- **Database ORM:** SQLModel 0.0.14+
- **Data Storage:** Neon Serverless PostgreSQL
- **Security:** JWT via python-jose
- **Encryption:** Passlib with bcrypt
- **AI Engine:** OpenAI Agents SDK with MCP Tools
- **Schema Migrations:** Alembic
- **Dependency Management:** uv

## Core Capabilities

- **Secure Access Control** - Token-based authentication with registration and session management
- **Complete Task Operations** - Create, read, update, and delete functionality
- **Intelligent Assistant** - Natural language processing for task interactions
- **Tool Integration** - Five specialized MCP tools for AI-driven operations
- **Persistent Conversations** - Full chat history retention in database
- **User Data Privacy** - Isolated workspaces for each user account

## Directory Organization

```
backend/
├── src/
│   ├── api/                  # HTTP route handlers
│   │   ├── auth.py           # User session management
│   │   ├── tasks.py          # Traditional task operations
│   │   ├── chat.py           # AI conversation interface
│   │   ├── conversations.py  # Conversation lifecycle
│   │   └── dependencies.py   # Authentication middleware
│   ├── core/                 # Foundation modules
│   │   ├── config.py         # App configuration
│   │   ├── database.py       # DB connection handling
│   │   └── security.py       # Token and hash utilities
│   ├── middleware/           # Request/response processors
│   │   ├── logging.py        # Activity tracking
│   │   └── errors.py         # Exception management
│   ├── models/               # Data structures
│   │   ├── user.py           # Account model
│   │   ├── task.py           # Task entity
│   │   ├── conversation.py   # Chat session model
│   │   └── message.py        # Individual message model
│   ├── services/             # Core business logic
│   │   ├── auth.py           # Authentication operations
│   │   ├── tasks.py          # Task management logic
│   │   ├── chat.py           # Conversation coordination
│   │   └── conversations.py  # Session management
│   ├── mcp/                  # AI integration layer
│   │   ├── agent.py          # OpenAI configuration
│   │   └── tools.py          # Tool implementations
│   └── main.py               # App initialization
├── alembic/                  # Schema versioning
├── tests/                    # Test suites
└── pyproject.toml            # Package configuration
```

## Configuration Requirements

Set up a `.env` file within the `backend/` folder:

```bash
# Database Connection
DATABASE_URL=postgresql://user:password@host.neon.tech/dbname?sslmode=require

# Authentication Settings
JWT_SECRET=your-secret-key-here-minimum-32-characters-required
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# AI Service (for conversational mode)
OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_MODEL=gpt-4.1-2025-04-14

# Cross-Origin Configuration
CORS_ORIGINS=http://localhost:3000

# General Settings
APP_NAME=Advanced Todo API
APP_VERSION=1.0.0
DEBUG=True

# Network Configuration
HOST=0.0.0.0
PORT=8000
```

## Getting Started

### System Requirements

- Python 3.11 or higher
- uv package manager: `pip install uv`
- Active Neon PostgreSQL account: https://neon.tech
- Valid OpenAI API credentials: https://platform.openai.com

### Initial Setup

```bash
# Change to backend folder
cd backend

# Set up dependencies (auto-creates .venv)
uv sync

# Prepare environment configuration
cp .env.example .env
# Update .env with your actual credentials
```

### Database Initialization

```bash
# Execute schema migrations
uv run alembic upgrade head
```

### Launch Development Server

```bash
# Start with hot-reload enabled
uv run uvicorn src.main:app --reload --port 8000
```

Access points after launch:
- **API Root:** http://localhost:8000
- **Interactive Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## Route Specifications

### User Authentication

| HTTP Method | Route | Purpose |
|-------------|-------|---------|
| POST | `/api/auth/register` | Create new account |
| POST | `/api/auth/login` | Authenticate user |
| POST | `/api/auth/logout` | End session (authenticated) |
| GET | `/api/auth/me` | Retrieve user details |
| PUT | `/api/auth/me` | Modify user information |

### Task Operations (Traditional Interface)

Authentication required for all task endpoints.

| HTTP Method | Route | Purpose |
|-------------|-------|---------|
| GET | `/api/tasks` | Fetch user's task list |
| POST | `/api/tasks` | Add new task |
| GET | `/api/tasks/{task_id}` | Retrieve single task |
| PUT | `/api/tasks/{task_id}` | Modify task details |
| DELETE | `/api/tasks/{task_id}` | Remove task |
| PATCH | `/api/tasks/{task_id}/complete` | Update completion state |

### Conversational Interface

| HTTP Method | Route | Purpose |
|-------------|-------|---------|
| POST | `/api/chat/chat` | Process user message |
| GET | `/api/chat/conversations` | Retrieve chat history |

### Session Management

| HTTP Method | Route | Purpose |
|-------------|-------|---------|
| GET | `/api/conversations` | View all sessions |
| POST | `/api/conversations` | Initialize new session |
| GET | `/api/conversations/{id}` | Load session details |
| PUT | `/api/conversations/{id}` | Update session title |
| DELETE | `/api/conversations/{id}` | Remove session |

## AI Tool Definitions

Five MCP tools enable intelligent task operations:

| Tool Name | Function | Required Parameters |
|-----------|----------|---------------------|
| `add_task` | Initialize task | `title`, `description?` |
| `list_tasks` | Retrieve tasks | `completed?` (optional filter) |
| `complete_task` | Update status | `task_identifier` |
| `update_task` | Modify details | `task_identifier`, `title?`, `description?` |
| `delete_task` | Delete task | `task_identifier` |

**Security Note:** User identity extracted from JWT token exclusively, never from client requests.

## Data Schema

```
users
├── id (UUID, PK)
├── email (unique, indexed)
├── hashed_password
├── full_name
├── profile_picture
├── is_active
├── created_at
└── updated_at

tasks
├── id (UUID, PK)
├── user_id (FK → users.id)
├── title
├── description
├── is_completed
├── created_at
└── updated_at

conversations
├── id (UUID, PK)
├── user_id (FK → users.id)
├── title
├── created_at
└── updated_at

messages
├── id (UUID, PK)
├── conversation_id (FK → conversations.id)
├── role ('user' | 'assistant')
├── content
└── created_at
```

## Schema Management

```bash
# Generate new migration
uv run alembic revision --autogenerate -m "description"

# Execute pending migrations
uv run alembic upgrade head

# Revert last migration
uv run alembic downgrade -1
```

## Security Measures

- Session tokens valid for 24 hours (configurable)
- Password encryption using bcrypt (rounds: 12)
- User workspace isolation at service layer
- Authentication mandatory for protected routes
- CORS restricted to approved origins
- User identification via JWT validation only

## Production Deployment Guide

1. Disable debug mode: `DEBUG=False`
2. Generate strong `JWT_SECRET` (32+ characters)
3. Configure production `DATABASE_URL`
4. Set production `OPENAI_API_KEY`
5. Define appropriate `CORS_ORIGINS`
6. Deploy with production-grade server

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Error Response Format

Standardized error structure:

```json
{
  "detail": "Human-readable error message"
}
```

HTTP status codes:
- `200` - Operation successful
- `201` - Resource created
- `204` - Deletion confirmed
- `400` - Invalid request data
- `401` - Authentication failed
- `404` - Resource not found
- `500` - Server error