import json

from nameko.events import EventDispatcher
from nameko.rpc import rpc

from services import _get_all_products, _get_product, _create_product


class ProductsService:
    name = 'products'

    event_dispatcher = EventDispatcher()

    @rpc
    def get_all_products(self):
        return _get_all_products()

    @rpc
    def get_product(self, product_id):
        return _get_product(product_id)

    @rpc
    def create_product(self, product_details):
        product = json.loads(product_details)
        _create_product(product)
        return {'detail': 'success'}
