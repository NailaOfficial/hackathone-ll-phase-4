# Task Management Interface - Client Application

Modern React-based frontend offering seamless interaction through both conversational chat and traditional forms.

## Technical Stack

- **Core Framework:** Next.js 16 with App Router
- **Type System:** TypeScript 5.x with strict mode
- **Design System:** Tailwind CSS 4
- **Component Library:** shadcn/ui built on Radix UI
- **Iconography:** Lucide React
- **User Feedback:** Sonner toast notifications
- **Package Manager:** pnpm

## Interaction Paradigms

Two complementary user experience modes:

### Conversational Mode (Chat-First)
- ChatGPT-inspired messaging interface
- Task manipulation through natural language
- Persistent conversation threads with navigation
- AI-assisted task workflows

### Traditional Mode (Form-Based)
- Classic input forms and action buttons
- Visual task list with interactive elements
- Modal-based editing and deletion
- Direct database operations

## Application Structure

```
frontend/
├── src/
│   ├── app/                        # App Router architecture
│   │   ├── page.tsx                # Landing and main application
│   │   ├── layout.tsx              # Root component wrapper
│   │   ├── globals.css             # Global styling rules
│   │   └── (auth)/                 # Auth route group
│   │       ├── login/              # Sign-in interface
│   │       ├── register/           # Account creation
│   │       └── layout.tsx          # Auth-specific layout
│   ├── components/
│   │   ├── chat/                   # Conversational UI
│   │   │   ├── ChatLayout.tsx      # Main chat container
│   │   │   ├── Sidebar.tsx         # Thread navigation panel
│   │   │   ├── ConversationItem.tsx # Thread list item
│   │   │   └── WelcomeScreen.tsx   # Initial chat state
│   │   ├── tasks/                  # Traditional UI
│   │   │   ├── TasksView.tsx       # Task mode wrapper
│   │   │   ├── TaskList.tsx        # Task collection view
│   │   │   ├── TaskItem.tsx        # Individual task display
│   │   │   ├── TaskForm.tsx        # Task creation interface
│   │   │   ├── EditTaskDialog.tsx  # Modification modal
│   │   │   └── DeleteTaskDialog.tsx # Removal confirmation
│   │   ├── navigation/             # App navigation
│   │   │   ├── AppHeader.tsx       # Top navigation bar
│   │   │   └── ModeToggle.tsx      # Interface switcher
│   │   ├── ui/                     # Base UI components
│   │   ├── ChatInterface.tsx       # Message display area
│   │   ├── ChatInput.tsx           # Message composition
│   │   ├── ChatMessage.tsx         # Message bubble component
│   │   ├── AuthForm.tsx            # Authentication UI
│   │   ├── ErrorBoundary.tsx       # Error recovery
│   │   └── Providers.tsx           # Context providers
│   ├── lib/                        # Shared utilities
│   │   ├── api.ts                  # Backend communication
│   │   ├── auth.ts                 # Session management
│   │   └── utils.ts                # Helper functions
│   └── types/                      # Type definitions
│       ├── task.ts                 # Task type schema
│       └── chat.ts                 # Chat type schema
├── package.json                    # Project dependencies
├── tsconfig.json                   # TypeScript settings
└── tailwind.config.ts              # Tailwind configuration
```

## Environment Setup

Create `.env.local` in the `frontend/` directory:

```bash
# API endpoint
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Installation Guide

### Prerequisites

- Node.js version 18 or later
- pnpm: Install with `npm install -g pnpm`

### Setup Process

```bash
# Navigate to client directory
cd frontend

# Install project dependencies
pnpm install

# Configure environment
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

### Development Workflow

```bash
# Launch dev server with hot reload
pnpm dev

# Application runs at http://localhost:3000
```

### Production Deployment

```bash
# Create optimized build
pnpm build

# Serve production build
pnpm start

# Run type validation
pnpm type-check

# Execute linter
pnpm lint
```

## Feature Overview

### User Access Control
- Account registration with input validation
- Token-based authentication
- Route-level access protection
- Smart navigation redirects
- Session termination

### Conversational Features
- Message-based task interaction
- Thread sidebar with CRUD operations
- Session initialization
- Welcome prompts for new users
- Tool-powered AI responses
- Loading state indicators

### Traditional Interface Features
- Form-based task creation
- Personal task inventory
- One-click completion toggle
- Edit functionality via dialogs
- Confirmation-protected deletion
- Per-user data isolation
- Optimistic UI rendering

### User Experience Polish
- Skeleton loading states
- Graceful error recovery
- Toast notification system
- Mobile-responsive layouts
- Helpful empty states
- Smooth mode transitions

## API Client Usage

Type-safe backend integration via `lib/api.ts`:

```typescript
import { authApi, tasksApi, chatApi, conversationsApi } from "@/lib/api";

// User authentication
await authApi.register({ email, password });
await authApi.login({ email, password });
await authApi.logout();
await authApi.getProfile();

// Task management (traditional mode)
const tasks = await tasksApi.getAll();
const task = await tasksApi.create({ title, description });
await tasksApi.update(taskId, { title, description });
await tasksApi.delete(taskId);
await tasksApi.toggleComplete(taskId);

// Conversational interface
const response = await chatApi.sendMessage("Add a task", conversationId);
const history = await chatApi.getConversation(conversationId);

// Thread management
const conversations = await conversationsApi.list();
await conversationsApi.rename(id, "New Title");
await conversationsApi.delete(id);
```

## Component Hierarchy

### Interface Switching Logic
```
Root Page (page.tsx)
├── Unauthenticated → Marketing Page
└── Authenticated → Application Shell
    ├── AppHeader (mode switch + user dropdown)
    └── Main Content
        ├── Chat Active → ChatLayout
        └── Tasks Active → TasksView
```

### Chat Interface Tree
```
ChatLayout
├── Sidebar (thread browser)
│   └── ConversationItem
└── ChatInterface
    ├── WelcomeScreen (empty state)
    ├── ChatMessage (conversation flow)
    └── ChatInput
```

### Task Interface Tree
```
TasksView
├── TaskForm (creation interface)
└── TaskList
    └── TaskItem
        ├── EditTaskDialog
        └── DeleteTaskDialog
```

## Type Safety Configuration

Strict TypeScript rules enforced:
- `strict: true`
- `noUnusedLocals: true`
- `noUnusedParameters: true`
- `noUncheckedIndexedAccess: true`

## Cloud Deployment

### Vercel Platform (Recommended)

1. Connect repository to Vercel
2. Import project from GitHub
3. Configure environment:
   - `NEXT_PUBLIC_API_URL` - Production API endpoint
4. Deploy application

Application will be live on Vercel's CDN with automatic HTTPS.