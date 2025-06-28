# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv pip install -e .
CMD ["python", "app/main.py"]
