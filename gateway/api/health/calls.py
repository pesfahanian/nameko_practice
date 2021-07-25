from multiprocessing.context import TimeoutError

from nameko.standalone.rpc import ClusterRpcProxy

from settings import CLUSTER_RPC, HEALTHCHECK_TIMEOUT

from utils import timeout


def healthcheck() -> None:
    try:
        return products_healthcheck()
    except TimeoutError:
        raise Exception(
            'Timeout in communicating with the `Products` service')
    except Exception as e:
        message = f'`Products` service healthcheck failed due to `{str(e)}`'
        raise Exception(message)


@timeout(HEALTHCHECK_TIMEOUT)
def products_healthcheck() -> None:
    with ClusterRpcProxy(CLUSTER_RPC) as rpc:
        result = rpc.products.healthcheck()
    if (result['status'] == 'ok'):
        return result
    else:
        raise Exception(result['status'])
