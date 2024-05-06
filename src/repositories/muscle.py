from typing import List
from src.schemas.muscle import Muscle
from src.models.muscle import Muscle as muscles

class MuscleRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_muscles(self) -> List[Muscle]:
        query = self.db.query(muscles)
        return query.all()
    
    def get_muscle_by_id(self, id: int ):
        element = self.db.query(muscles).filter(muscles.id == id).first()
        return element
    
    def delete_muscle(self, id: int ) -> dict:
        element: Muscle= self.db.query(muscles).filter(muscles.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_muscle(self, muscle:Muscle ) -> dict:
        new_muscle = muscles(**muscle.model_dump())
        self.db.add(new_muscle)
        
        self.db.commit()
        self.db.refresh(new_muscle)
        return new_muscle
    
    def update_muscle(self, id: int, muscle: Muscle) -> dict:
        element = self.db.query(muscles).filter(muscles.id == id).first()
        element.name = muscle.name
        element.description = muscle.description

        self.db.commit()
        self.db.refresh(element)
        return element