from sqlalchemy import Column, Integer, Boolean, String

from database.connection import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    in_stock = Column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()
