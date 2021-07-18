from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from nameko.standalone.rpc import ClusterRpcProxy

from api.products.schema import Product
from api.products.urls import PRODUCTS_ENDPOINT

from settings import CLUSTER_RPC

router = APIRouter(prefix=PRODUCTS_ENDPOINT,
                   tags=['Products'],
                   responses={404: {
                       'description': 'Not found.'
                   }})


@router.get('/', status_code=200)
def get_all_product() -> JSONResponse:
    try:
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            result = rpc.products.get_all_products()
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
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            result = rpc.products.get_product(product_id)
    except Exception as e:
        message = f'Failed to get product. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)

    content = {
        'result': result,
    }
    return JSONResponse(status_code=200, content=content)


@router.post('/', status_code=200)
def create_product(product: Product) -> JSONResponse:
    try:
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            result = rpc.products.create_product(product.json())
    except Exception as e:
        message = f'Failed to create product. Reason: {str(e)}.'
        raise HTTPException(status_code=400, detail=message)

    content = {
        'result': result,
    }
    return JSONResponse(status_code=200, content=content)
