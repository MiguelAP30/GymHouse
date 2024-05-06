from typing import List
from src.schemas.type_quantity import TypeQuantity
from src.models.type_quantity import TypeQuantity as type_quantities

class TypeQuantityRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_type_quantities(self) -> List[TypeQuantity]:
        query = self.db.query(type_quantities)
        return query.all()
    
    def get_type_quantity_by_id(self, id: int ):
        element = self.db.query(type_quantities).filter(type_quantities.id == id).first()
        return element
    
    def delete_type_quantity(self, id: int ) -> dict:
        element: TypeQuantity= self.db.query(type_quantities).filter(type_quantities.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_type_quantity(self, type_quantity:TypeQuantity ) -> dict:
        new_type_quantity = type_quantities(**type_quantity.model_dump())
        self.db.add(new_type_quantity)
        
        self.db.commit()
        self.db.refresh(new_type_quantity)
        return new_type_quantity
    
    def update_type_quantity(self, id: int, type_quantity: TypeQuantity) -> dict:
        element = self.db.query(type_quantities).filter(type_quantities.id == id).first()
        element.name = type_quantity.name
        element.description = type_quantity.description

        self.db.commit()
        self.db.refresh(element)
        return element