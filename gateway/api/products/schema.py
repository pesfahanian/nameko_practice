from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    in_stock: bool = True
