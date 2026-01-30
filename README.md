# Intelligent Task Manager - Full Stack Application

A next-generation productivity platform combining **conversational AI** and **traditional interfaces** for flexible task management. Built with specification-driven architecture principles.

## Standout Capabilities

- **Flexible Interaction Modes** - Work your way:
  - **Chat Interface**: Manage tasks through natural conversation
  - **Classic Interface**: Use familiar forms and visual controls
- **Instant Mode Switching** - Change interfaces without losing context
- **OpenAI Integration** - Smart understanding of task-related language
- **Secure Multi-Tenancy** - Complete data isolation per user account
- **Live Synchronization** - Changes reflect immediately across both modes

## System Architecture

**Monorepo Organization:**
- `backend/` - Python FastAPI service with AI agent and JWT security
- `frontend/` - TypeScript Next.js app with dual interface modes
- `specs/` - Technical specifications and planning documents
- `.specify/` - Spec-Kit Plus tooling and templates

## Development Stack

### Server-Side
- **Web Framework:** FastAPI 0.125+
- **Database Layer:** SQLModel 0.0.14+
- **Storage:** Neon Serverless PostgreSQL
- **Session Management:** JWT via python-jose
- **AI Platform:** OpenAI Agents SDK with MCP Tools
- **Credential Security:** Passlib with bcrypt
- **Package Manager:** uv

### Client-Side
- **UI Framework:** Next.js 16 with App Router
- **Programming Language:** TypeScript 5.x (strict)
- **CSS Framework:** Tailwind CSS 4
- **Component System:** shadcn/ui on Radix UI
- **User Notifications:** Sonner
- **Package Manager:** pnpm

## Platform Features

### Chat-Based Interaction
- Natural language task entry ("Create a task for team meeting")
- Query your tasks conversationally ("What do I need to do today?")
- Mark items complete via chat ("Done with team meeting")
- Update and remove tasks through conversation
- Thread history persistence
- Context-aware multi-turn dialogue

### Visual Interface
- Structured form for task entry
- Interactive task list with status indicators
- Edit operations through modal dialogs
- Confirmation dialogs for destructive actions
- Visual completion feedback
- Progressive loading patterns

### Cross-Cutting Features
- Token-based user authentication
- Protected account creation and access
- User profile customization
- Mobile and desktop responsive design
- System-wide toast feedback
- Resilient error handling

## System Requirements

- **Python 3.11+** (backend service)
- **Node.js 18+** (frontend application)
- **uv** (Python tooling): Install via `pip install uv`
- **pnpm** (Node tooling): Install via `npm install -g pnpm`
- **Neon Database**: Create account at https://neon.tech
- **OpenAI API**: Required for conversational features

## Deployment Strategies

### Local Development Environment
Detailed instructions available in [specs/003-combined-cui-gui/quickstart.md](specs/003-combined-cui-gui/quickstart.md).

### Docker Compose Stack
Containerized local deployment:

```bash
# Prepare environment configuration
cp .env.example .env
# Edit .env: Add OPENAI_API_KEY and JWT_SECRET

# Launch entire stack
docker-compose up -d

# Access services
# Web App: http://localhost:3000
# API Server: http://localhost:8000
```

### Kubernetes Cluster (Minikube)
Production-like orchestration with Helm:

```bash
# Deploy on Minikube (Unix-based systems)
./scripts/deploy-minikube.sh --openai-key "sk-your-key"

# Deploy on Minikube (Windows systems)
.\scripts\deploy-minikube.ps1 -OpenAIKey "sk-your-key"

# Validate deployment status
./scripts/verify-deployment.sh  # or .ps1 on Windows
```

Refer to [Kubernetes Deployment](#kubernetes-orchestration) for comprehensive details.

## Quick Start Process

### Backend Configuration

```bash
cd backend

# Initialize dependencies (auto-creates virtual env)
uv sync

# Set up environment
cp .env.example .env
# Required configuration:
# - DATABASE_URL (Neon connection string)
# - JWT_SECRET (cryptographically random string)
# - OPENAI_API_KEY (API credentials)

# Initialize database schema
uv run alembic upgrade head

# Start API server
uv run uvicorn src.main:app --reload --port 8000
```

API available at http://localhost:8000
Documentation at http://localhost:8000/docs

### Frontend Configuration

```bash
cd frontend

# Install packages
pnpm install

# Configure backend URL
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Launch web server
pnpm dev
```

Application available at http://localhost:3000

## Repository Layout

```
phase-4/
├── backend/
│   ├── src/
│   │   ├── models/          # Data models (User, Task, Conversation, Message)
│   │   ├── services/        # Core logic layer
│   │   ├── api/             # HTTP endpoints (auth, tasks, chat, conversations)
│   │   ├── mcp/             # AI integration and tools
│   │   ├── core/            # Config, security, database
│   │   └── middleware/      # Request processing, errors
│   ├── alembic/             # Schema migrations
│   ├── Dockerfile           # Backend container
│   └── pyproject.toml       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js routing
│   │   ├── components/
│   │   │   ├── chat/        # Chat UI (ChatLayout, Sidebar, etc.)
│   │   │   ├── tasks/       # Task UI (TaskList, TaskForm, etc.)
│   │   │   ├── navigation/  # Header, mode switcher
│   │   │   └── ui/          # Base components
│   │   ├── lib/             # API client, utilities
│   │   └── types/           # Type definitions
│   ├── Dockerfile           # Frontend container
│   └── package.json         # Node dependencies
├── helm/
│   └── taskai/              # Kubernetes package
│       ├── Chart.yaml       # Chart info
│       ├── values.yaml      # Default config
│       └── templates/       # K8s resources
├── scripts/
│   ├── deploy-minikube.sh   # Unix deployment script
│   ├── deploy-minikube.ps1  # Windows deployment script
│   ├── verify-deployment.sh # Unix verification
│   └── verify-deployment.ps1# Windows verification
├── specs/
│   ├── 001-todo-app-baseline/    # Phase-2 specification
│   ├── 002-todo-ai-chatbot/      # Phase-3 specification
│   └── 003-combined-cui-gui/     # Phase-4 specification
├── docker-compose.yml       # Local container orchestration
├── .env.example             # Environment template
└── .specify/                # Spec-Kit configuration
```

## Usage Patterns

### Interface Navigation
1. Authenticate to access main application
2. Locate **Chat** / **Tasks** toggle in header
3. Switch freely - data remains synchronized

### Conversational Examples
```
User: "Create a task for quarterly review"
AI: "Task created successfully: 'quarterly review'"

User: "What tasks do I have?"
AI: "Here are your active tasks:
     1. quarterly review (pending)
     2. update documentation (completed)
     3. client followup (pending)"

User: "Complete the quarterly review"
AI: "Marked 'quarterly review' as completed."
```

### Visual Interface Flow
- Select "Tasks" to switch modes
- Fill out form for new tasks
- Click checkboxes to mark complete
- Use action buttons for editing/deletion

## API Reference

Interactive documentation available when backend is running:
- **Swagger Interface**: http://localhost:8000/docs
- **ReDoc Interface**: http://localhost:8000/redoc

### Primary Routes

| Route | Method | Function |
|-------|--------|----------|
| `/api/auth/register` | POST | Create account |
| `/api/auth/login` | POST | Authenticate |
| `/api/tasks` | GET | Retrieve tasks (visual mode) |
| `/api/tasks` | POST | Create task (visual mode) |
| `/api/chat/chat` | POST | Process message (chat mode) |
| `/api/conversations` | GET | List conversations (chat mode) |

## Security Architecture

- JWT authentication with 24-hour validity
- Bcrypt password hashing (12 rounds)
- User-level data isolation in database and API
- HTTPS enforcement in production
- Environment-based secret management
- Tool-based user verification (never client input)

## Governance Framework

Follows rigorous **Specification-Driven Development** methodology:

1. **Spec-First Approach**: Documentation precedes implementation
2. **Centralized Code Authority**: Claude Code handles all coding
3. **Clear Module Boundaries**: Distinct backend/frontend/chat/visual layers
4. **Mandatory Authentication**: JWT required for protected operations
5. **Stateless Architecture**: PostgreSQL as single source of truth
6. **Tool-Mediated AI**: Conversational operations exclusively through MCP

Complete governance rules in `.specify/memory/constitution.md`.

## Reference Documentation

- **Feature Specification**: `specs/003-combined-cui-gui/spec.md`
- **Execution Plan**: `specs/003-combined-cui-gui/plan.md`
- **Work Breakdown**: `specs/003-combined-cui-gui/tasks.md`
- **Schema Design**: `specs/003-combined-cui-gui/data-model.md`
- **Installation Guide**: `specs/003-combined-cui-gui/quickstart.md`

## Kubernetes Orchestration

### Required Tools

- **minikube** - Local K8s environment
- **kubectl** - Kubernetes command interface
- **helm** - Package management for K8s
- **docker** - Container engine

### Automated Deployment

Scripts include automatic port-forwarding for localhost access:

```bash
# Unix-based systems
./scripts/deploy-minikube.sh

# Windows systems
.\scripts\deploy-minikube.ps1
```

**Post-deployment access points:**
- Web Interface: http://localhost:3000 (Unix) or http://localhost:4000 (Windows)
- API Service: http://localhost:8080 (Unix) or http://localhost:5000 (Windows)
- API Docs: http://localhost:8080/docs or http://localhost:5000/docs

### Manual Orchestration

```bash
# Initialize Minikube cluster
minikube start --cpus=4 --memory=8192

# Configure Docker environment
eval $(minikube docker-env)  # Unix
minikube docker-env --shell powershell | Invoke-Expression  # Windows

# Build container images
docker build -t taskai-backend:latest ./backend
docker build --build-arg NEXT_PUBLIC_API_URL="http://localhost:8080" \
  -t taskai-frontend:latest ./frontend

# Deploy via Helm
helm upgrade --install taskai ./helm/taskai \
  --namespace taskai \
  --create-namespace \
  --set secrets.openaiApiKey="sk-your-key"

# Check deployment health
kubectl get pods -n taskai
```

### Service Access Points

Port-forwarding enabled (automatic with deployment scripts):

| Component | Unix URL | Windows URL |
|-----------|----------|-------------|
| Web Application | http://localhost:3000 | http://localhost:4000 |
| API Service | http://localhost:8080 | http://localhost:5000 |
| API Documentation | http://localhost:8080/docs | http://localhost:5000/docs |

> **Note:** Port-forwarding runs as background processes. See script output for termination commands.

### Helm Configuration

Key settings in `helm/taskai/values.yaml`:

```yaml
secrets:
  jwtSecret: "your-jwt-secret"
  openaiApiKey: "sk-your-key"

frontend:
  service:
    port: 3000  # Via port-forwarding

backend:
  service:
    port: 8000  # Via port-forwarding (local:8080 -> service:8000)
  env:
    OPENAI_MODEL: "gpt-4.1-2025-04-14"
```

### Management Commands

```bash
# List running pods
kubectl get pods -n taskai

# Stream logs
kubectl logs -f deploy/taskai-backend -n taskai

# Inspect pod details
kubectl describe pod <pod-name> -n taskai

# Launch dashboard
minikube dashboard

# Remove deployment
helm uninstall taskai -n taskai
kubectl delete namespace taskai
```

## Docker Compose Alternative

Simplified local setup without Kubernetes:

```bash
# Start services
docker-compose up -d

# Monitor output
docker-compose logs -f

# Stop services
docker-compose down

# Stop with data cleanup
docker-compose down -v
```

### Service Endpoints

| Component | Port | Description |
|-----------|------|-------------|
| frontend | 3000 | Next.js interface |
| backend | 8000 | FastAPI service |
| postgres | 5432 | PostgreSQL database |

## Contribution Guidelines

This project uses Spec-Kit Plus methodology. Contributions require:
1. Specification creation (`/sp.specify`)
2. Implementation planning (`/sp.plan`)
3. Task breakdown (`/sp.tasks`)
4. Code implementation (`/sp.implement`)

See `.specify/` for detailed templates and workflows.