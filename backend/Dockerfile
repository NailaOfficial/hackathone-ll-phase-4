FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

RUN pip install --upgrade pip && pip install .

COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini ./

WORKDIR /app/src

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
