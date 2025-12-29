import logging
import json
import time
from fastapi import Request

logger = logging.getLogger('app')


total_requests = 0
start_time = time.time()

async def logging_middleware(request:Request,call_next):
    global total_requests
    total_requests += 1

    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    logger.info(json.dumps({
        'event':'http_request',
        'method':request.method,
        'path':request.url.path,
        'status_code':response.status_code,
        'duration_ms':round(duration * 1000,2)
    }))

    return response