from typing import List
from src.schemas.plate import Plate
from src.models.plate import Plate as plates

class PlateRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_plates(self) -> List[Plate]:
        query = self.db.query(plates)
        return query.all()
    
    def get_plate_by_id(self, id: int ):
        element = self.db.query(plates).filter(plates.id == id).first()
        return element
    
    def delete_plate(self, id: int ) -> dict:
        element: Plate= self.db.query(plates).filter(plates.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_plate(self, plate:Plate ) -> dict:
        new_plate = plates(**plate.model_dump())
        self.db.add(new_plate)
        
        self.db.commit()
        self.db.refresh(new_plate)
        return new_plate
    
    def get_plate_by_name(self, name: str):
        element = self.db.query(plates).filter(plates.name == name).first()
        return element
    
    def update_plate(self, id: int, plate: Plate) -> dict:
        element = self.db.query(plates).filter(plates.id == id).first()
        element.name = plate.name
        element.description = plate.description

        self.db.commit()
        self.db.refresh(element)
        return element