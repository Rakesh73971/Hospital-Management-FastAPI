# Logging & Monitoring API

## Features
- Structured logging (JSON format)
- Health check endpoint
- Metrics endpoint

## Endpoints
- GET /health
- GET /metrics

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
