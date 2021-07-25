from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.health.calls import healthcheck

from api.products.calls import _get_all_products, _get_product, _add_product
from api.products.schema import Product
from api.products.urls import PRODUCTS_ENDPOINT

router = APIRouter(prefix=PRODUCTS_ENDPOINT,
                   tags=['Products'],
                   responses={404: {
                       'description': 'Not found.'
                   }})


@router.get('/', status_code=200)
def get_all_products() -> JSONResponse:
    try:
        healthcheck()
        result = _get_all_products()
    except Exception as e:
        message = f'Failed to get all products. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)

    content = {
        'result': result,
    }
    return JSONResponse(status_code=200, content=content)


@router.get('/product/', status_code=200)
def get_product(product_id: int) -> JSONResponse:
    try:
        healthcheck()
        result = _get_product(product_id=product_id)
    except Exception as e:
        message = f'Failed to get product. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)

    content = {
        'result': result,
    }
    return JSONResponse(status_code=200, content=content)


@router.post('/', status_code=200)
def add_product(product: Product) -> JSONResponse:
    try:
        healthcheck()
        result = _add_product(product=product)
    except Exception as e:
        message = f'Failed to create product. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)

    content = {
        'result': result,
    }
    return JSONResponse(status_code=200, content=content)
