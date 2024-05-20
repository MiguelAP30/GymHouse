from typing import List
from src.schemas.training_plan import TrainingPlan
from src.models.training_plan import TrainingPlan as training_plans
from src.models.training_plan_user import TrainingPlanUser as training_plan_user

class TrainingPlanRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase TrainingPlanRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se crea una instancia de TrainingPlanRepository con el objeto de la base de datos asignado.
        """
        self.db = db
    
    def get_all_training_plans(self, user: str) -> List[TrainingPlan]:
        """
        Obtiene todos los planes de entrenamiento asociados a un usuario.

        Parámetros:
        - user: correo electrónico del usuario.

        Precondición:
        - El usuario debe existir en la base de datos.

        Postcondición:
        - Devuelve una lista de objetos TrainingPlan que representan los planes de entrenamiento asociados al usuario.
        """
        query = self.db.query(training_plans).join(training_plan_user).filter(training_plan_user.user_email == user)
        return query.all()
    
    def get_training_plan_by_id(self, id: int, user: str):
        """
        Obtiene un plan de entrenamiento por su ID y usuario asociado.

        Parámetros:
        - id: ID del plan de entrenamiento.
        - user: correo electrónico del usuario.

        Precondición:
        - El plan de entrenamiento con el ID especificado debe existir en la base de datos.
        - El usuario debe existir en la base de datos.

        Postcondición:
        - Devuelve el objeto TrainingPlan que representa el plan de entrenamiento solicitado.
        """
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        return element
    
    def delete_training_plan(self, id: int, user: str) -> dict:
        """
        Elimina un plan de entrenamiento por su ID y usuario asociado.

        Parámetros:
        - id: ID del plan de entrenamiento.
        - user: correo electrónico del usuario.

        Precondición:
        - El plan de entrenamiento con el ID especificado debe existir en la base de datos.
        - El usuario debe existir en la base de datos.

        Postcondición:
        - El plan de entrenamiento se elimina de la base de datos.
        - Devuelve un diccionario que representa el plan de entrenamiento eliminado.
        """
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan(self, training_plan:TrainingPlan ) -> dict:
        """
        Crea un nuevo plan de entrenamiento.

        Parámetros:
        - training_plan: objeto TrainingPlan que representa el nuevo plan de entrenamiento.

        Precondición:
        - Ninguna.

        Postcondición:
        - El nuevo plan de entrenamiento se crea en la base de datos.
        - Devuelve un diccionario que representa el nuevo plan de entrenamiento creado.
        """
        new_training_plan = training_plans(**training_plan.model_dump())
        self.db.add(new_training_plan)
        self.db.commit()
        self.db.refresh(new_training_plan)
        return new_training_plan

    def update_training_plan(self, id: int, training_plan: TrainingPlan, user: str) -> dict:    
        """
        Actualiza un plan de entrenamiento por su ID y usuario asociado.

        Parámetros:
        - id: ID del plan de entrenamiento.
        - training_plan: objeto TrainingPlan que representa los nuevos datos del plan de entrenamiento.
        - user: correo electrónico del usuario.

        Precondición:
        - El plan de entrenamiento con el ID especificado debe existir en la base de datos.
        - El usuario debe existir en la base de datos.

        Postcondición:
        - El plan de entrenamiento se actualiza en la base de datos con los nuevos datos proporcionados.
        - Devuelve un diccionario que representa el plan de entrenamiento actualizado.
        """
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        element.name = training_plan.name
        element.description = training_plan.description

        self.db.commit()
        self.db.refresh(element)
        return element