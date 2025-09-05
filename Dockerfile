# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (without dev deps)
RUN poetry install --no-root --only main

# Copy the rest of the project
COPY . /app

# Expose Django port
EXPOSE 8000

# Run server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
