from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.health.calls import healthcheck
from api.health.urls import HEALTH_ENDPOINT

router = APIRouter(prefix=HEALTH_ENDPOINT,
                   tags=['Health'],
                   responses={404: {
                       'description': 'Not found.'
                   }})


@router.get('/', status_code=200)
def check_health() -> JSONResponse:
    try:
        content = healthcheck()
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        message = f'Healthcheck failed. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)
