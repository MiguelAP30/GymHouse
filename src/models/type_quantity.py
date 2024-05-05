from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class TypeQuantity(Base):
    __tablename__ = "types_quantities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))

    quantity_foods = relationship("Quantity", back_populates="types_quantities")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}