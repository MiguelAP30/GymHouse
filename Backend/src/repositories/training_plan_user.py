from typing import List
from src.schemas.training_plan_user import TrainingPlanUser
from src.models.training_plan_user import TrainingPlanUser as training_plan_users

class TrainingPlanUserRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase TrainingPlanUserRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se crea una instancia de la clase TrainingPlanUserRepository.
        """
        self.db = db
    
    def get_all_training_plan_users(self, user: str) -> List[TrainingPlanUser]:
        """
        Obtiene todos los usuarios de planes de entrenamiento asociados a un usuario específico.

        Parámetros:
        - user: correo electrónico del usuario.

        Precondición:
        - El parámetro user debe ser una cadena de caracteres válida.

        Postcondición:
        - Devuelve una lista de objetos TrainingPlanUser asociados al usuario especificado.
        """
        query = self.db.query(training_plan_users).filter(training_plan_users.user_email == user)
        return query.all()
    
    def get_training_plan_user_by_id(self, id: int, user: str):
        """
        Obtiene un usuario de plan de entrenamiento por su ID y usuario asociado.

        Parámetros:
        - id: ID del usuario de plan de entrenamiento.
        - user: correo electrónico del usuario.

        Precondición:
        - El parámetro id debe ser un entero válido.
        - El parámetro user debe ser una cadena de caracteres válida.

        Postcondición:
        - Devuelve el objeto TrainingPlanUser correspondiente al ID y usuario especificados.
        """
        element = self.db.query(training_plan_users).filter(training_plan_users.id == id, training_plan_users.user_email == user).first()
        return element
    
    def delete_training_plan_user(self, id: int, user: str) -> dict:
        """
        Elimina un usuario de plan de entrenamiento por su ID y usuario asociado.

        Parámetros:
        - id: ID del usuario de plan de entrenamiento.
        - user: correo electrónico del usuario.

        Precondición:
        - El parámetro id debe ser un entero válido.
        - El parámetro user debe ser una cadena de caracteres válida.

        Postcondición:
        - Devuelve un diccionario con la información del usuario de plan de entrenamiento eliminado.
        """
        element: TrainingPlanUser= self.db.query(training_plan_users).filter(training_plan_users.id == id, training_plan_users.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan_user(self, training_plan_user:TrainingPlanUser ) -> dict:
        """
        Crea un nuevo usuario de plan de entrenamiento.

        Parámetros:
        - training_plan_user: objeto TrainingPlanUser con los datos del nuevo usuario de plan de entrenamiento.

        Precondición:
        - El parámetro training_plan_user debe ser un objeto válido de la clase TrainingPlanUser.

        Postcondición:
        - Crea un nuevo usuario de plan de entrenamiento en la base de datos y devuelve un diccionario con su información.
        """
        new_training_plan_user = training_plan_users(**training_plan_user.model_dump())
        self.db.add(new_training_plan_user)
        self.db.commit()
        self.db.refresh(new_training_plan_user)
        return new_training_plan_user