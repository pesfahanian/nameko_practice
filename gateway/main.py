from fastapi import FastAPI

from api.products import routers as products_routers

from settings import TITLE, VERSION 

app = FastAPI(title=TITLE, version=f'{VERSION}.0.0')

app.include_router(products_routers.router)
