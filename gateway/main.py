from fastapi import FastAPI

from api.health import routers as health_routers
from api.health.calls import healthcheck

from api.products import routers as products_routers

from settings import TITLE, VERSION

app = FastAPI(title=TITLE, version=f'{VERSION}.0.0')


@app.on_event('startup')
def startup():
    healthcheck()


app.include_router(health_routers.router)
app.include_router(products_routers.router)
