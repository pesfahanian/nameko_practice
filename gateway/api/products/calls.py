from nameko.standalone.rpc import ClusterRpcProxy

from api.products.schema import Product

from settings import CLUSTER_RPC


def _get_all_products() -> dict:
    try:
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            return rpc.products.get_all_products()
    except Exception as e:
        raise Exception(str(e))


def _get_product(product_id: int) -> dict:
    try:
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            return rpc.products.get_product(product_id)
    except Exception as e:
        raise Exception(str(e))


def _add_product(product: Product) -> dict:
    try:
        with ClusterRpcProxy(CLUSTER_RPC) as rpc:
            return rpc.products.add_product(product.json())
    except Exception as e:
        raise Exception(str(e))
