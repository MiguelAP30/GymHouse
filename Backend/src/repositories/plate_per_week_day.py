from typing import List
from src.schemas.plate_per_week_day import PlatePerWeekDay
from src.models.plate_per_week_day import PlatePerWeekDay as plate_per_week_days

class PlatePerWeekDayRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_plate_per_week_days(self) -> List[PlatePerWeekDay]:
        query = self.db.query(plate_per_week_days)
        return query.all()
    
    def get_plate_per_week_day_by_id(self, id: int ):
        element = self.db.query(plate_per_week_days).filter(plate_per_week_days.id == id).first()
        return element
    
    def delete_plate_per_week_day(self, id: int ) -> dict:
        element: PlatePerWeekDay= self.db.query(plate_per_week_days).filter(plate_per_week_days.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_plate_per_week_day(self, plate_per_week_day:PlatePerWeekDay ) -> dict:
        new_plate_per_week_day = plate_per_week_days(**plate_per_week_day.model_dump())
        self.db.add(new_plate_per_week_day)
        
        self.db.commit()
        self.db.refresh(new_plate_per_week_day)
        return new_plate_per_week_day