from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class TypeQuantity(Base):
    __tablename__ = "types_quantities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=30))
    description = Column(String(length=200))

    quantity_foods = relationship("QuantityFood", back_populates="types_quantities")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}