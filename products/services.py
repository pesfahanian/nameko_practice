from fastapi.encoders import jsonable_encoder

from database.connection import SQLite
from database.models import Product


def _get_all_products() -> list:
    session = SQLite().session
    products = session.query(Product).all()
    return [jsonable_encoder(product) for product in products]


def _get_product(product_id: int) -> dict:
    session = SQLite().session
    product = session.query(Product).filter(
        Product.id == int(product_id)).first()
    return jsonable_encoder(product)


def _create_product(product_details: dict) -> None:
    session = SQLite().session
    new_product = Product(id=product_details['id'],
                          name=product_details['name'],
                          in_stock=True)
    session.add(new_product)
    session.commit()
    return
