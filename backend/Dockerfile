FROM python:3.11-slim

WORKDIR /app

# Install uv for fast package installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_CACHE=1

# Step 1: Copy dependency files
COPY pyproject.toml uv.lock ./

# Step 2: Install dependencies (without cache mounts)
RUN uv sync --frozen --no-dev --no-install-project

# Step 3: Copy the rest of the code
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini ./

# Step 4: Install the project itself (without cache mounts)
RUN uv sync --frozen --no-dev

# Set working directory to src for correct imports
WORKDIR /app/src

# Expose port for Railway
EXPOSE 8000

# Run the app
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
