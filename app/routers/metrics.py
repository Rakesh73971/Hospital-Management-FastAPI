from fastapi import APIRouter
import time
from app.middleware import total_requests,start_time

router = APIRouter()

@router.get('/metrics')
def metrics():
    uptime = time.time() - start_time

    return {
        'uptime_seconds':round(uptime,2),
        'total_request':total_requests
    }