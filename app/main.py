from fastapi import FastAPI
from app.logging_config import setup_logging
from app.middleware import logging_middleware
from .routers.health import router as health_router
from .routers.metrics import router as metrics_router

setup_logging()

app = FastAPI(title='Logging & Monitoring API')

app.middleware('http')(logging_middleware)

app.include_router(health_router)
app.include_router(metrics_router)