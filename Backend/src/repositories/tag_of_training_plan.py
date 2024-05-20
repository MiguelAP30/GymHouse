from typing import List
from src.schemas.tag_of_training_plan import TagOfTrainingPlan
from src.models.tag_of_training_plan import TagOfTrainingPlan as tag_of_training_plans

class TagOfTrainingPlanRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_tag_of_training_plans(self) -> List[TagOfTrainingPlan]:
        """
        Obtiene todos los registros de la tabla tag_of_training_plans en la base de datos.
        
        Precondición:
        - No se requiere ninguna precondición.
        
        Postcondición:
        - Devuelve una lista de objetos TagOfTrainingPlan que representan todos los registros de la tabla.
        """
        query = self.db.query(tag_of_training_plans)
        return query.all()
    
    def get_tag_of_training_plan_by_id(self, id: int ):
        """
        Obtiene un registro de la tabla tag_of_training_plans por su ID.
        
        Precondición:
        - Se requiere un ID válido como parámetro.
        
        Postcondición:
        - Devuelve el objeto TagOfTrainingPlan correspondiente al ID proporcionado.
        """
        element = self.db.query(tag_of_training_plans).filter(tag_of_training_plans.id == id).first()
        return element
    
    def delete_tag_of_training_plan(self, id: int ) -> dict:
        """
        Elimina un registro de la tabla tag_of_training_plans por su ID.
        
        Precondición:
        - Se requiere un ID válido como parámetro.
        
        Postcondición:
        - Elimina el registro correspondiente al ID proporcionado de la base de datos.
        - Devuelve un diccionario que representa el registro eliminado.
        """
        element: TagOfTrainingPlan= self.db.query(tag_of_training_plans).filter(tag_of_training_plans.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_tag_of_training_plan(self, tag_of_training_plan:TagOfTrainingPlan ) -> dict:
        """
        Crea un nuevo registro en la tabla tag_of_training_plans.
        
        Precondición:
        - Se requiere un objeto TagOfTrainingPlan válido como parámetro.
        
        Postcondición:
        - Crea un nuevo registro en la base de datos con los datos proporcionados.
        - Devuelve un diccionario que representa el nuevo registro creado.
        """
        new_tag_of_training_plan = tag_of_training_plans(**tag_of_training_plan.model_dump())
        self.db.add(new_tag_of_training_plan)
        
        self.db.commit()
        self.db.refresh(new_tag_of_training_plan)
        return new_tag_of_training_plan
    
    def update_tag_of_training_plan(self, id: int, tag_of_training_plan: TagOfTrainingPlan) -> dict:    
        """
        Actualiza un registro de la tabla tag_of_training_plans por su ID.
        
        Precondición:
        - Se requiere un ID válido y un objeto TagOfTrainingPlan válido como parámetros.
        
        Postcondición:
        - Actualiza el registro correspondiente al ID proporcionado con los datos del objeto proporcionado.
        - Devuelve un diccionario que representa el registro actualizado.
        """
        element = self.db.query(tag_of_training_plans).filter(tag_of_training_plans.id == id).first()
        element.name = tag_of_training_plan.name

        self.db.commit()
        self.db.refresh(element)
        return element