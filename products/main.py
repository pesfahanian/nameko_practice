import json

from nameko.events import EventDispatcher
from nameko.rpc import rpc

from services import _get_all_products, _get_product, _add_product


class ProductsService:
    name = 'products'

    event_dispatcher = EventDispatcher()

    @rpc
    # todo: type hinting for args and return
    def healthcheck(self):
        return {'status': 'ok'}

    @rpc
    # todo: type hinting for args and return
    def get_all_products(self):
        return _get_all_products()

    @rpc
    # todo: type hinting for args and return
    def get_product(self, product_id):
        return _get_product(product_id)

    @rpc
    # todo: type hinting for args and return
    def add_product(self, product_details):
        product = json.loads(product_details)
        _add_product(product)
        return {'detail': 'Success'}
