import json
from fastapi import APIRouter, Response, HTTPException
import src.Controller as Controller
from src.Observability import *

HealthCheck = APIRouter()


@HealthCheck.get(path="/healthcheck")
def get_health():
    _ = get_current_span()
    headers = get_response_headers()
    try:
        response = Response(
            content=json.dumps(Controller.HealthCheck.get(), indent=4), headers=headers
        )
    except Exception as e:
        logger.exception(e, exc_info=True)
        raise HTTPException(status_code=500, detail=headers, headers=headers)
    else:
        set_current_span_status()
        return response
