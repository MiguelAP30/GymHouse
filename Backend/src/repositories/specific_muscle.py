from typing import List
from src.models.specific_muscle import SpecificMuscle as specific_muscle
from src.schemas.specific_muscle import SpecificMuscle

class SpecificMuscleRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase SpecificMuscleRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de SpecificMuscleRepository.
        """
        self.db = db

    def get_all_specific_muscle(self) -> List[SpecificMuscle]:
        """
        Obtiene todos los músculos específicos.

        Returns:
            Una lista de objetos SpecificMuscle que representan los músculos específicos.

        Postcondición:
            - Se devuelve una lista de objetos SpecificMuscle.
        """
        query = self.db.query(specific_muscle)
        return query.all()
    
    def create_new_specific_muscle(self, specific_muscle: SpecificMuscle) -> SpecificMuscle:
        """
        Crea un nuevo músculo específico.

        Args:
            specific_muscle: El objeto SpecificMuscle que representa el músculo específico a crear.

        Returns:
            El objeto SpecificMuscle creado.

        Precondición:
            - specific_muscle debe ser un objeto SpecificMuscle válido.

        Postcondición:
            - Se crea un nuevo músculo específico.
        """

        new_specific_muscle = specific_muscle(**specific_muscle.model_dump())
        self.db.add(new_specific_muscle)

        self.db.commit()
        self.db.refresh(new_specific_muscle)
        return new_specific_muscle
    
    def delete_specific_muscle(self, id: int) -> dict:
        """
        Elimina un músculo específico específico.
        """
        query = self.db.query(specific_muscle).filter(specific_muscle.id == id)
        result = query.first()
        self.db.delete(result)
        self.db.commit()
        return {"message": "The specific muscle was successfully deleted", "data": None}
    
    def update_specific_muscle(self, id: int, specific_muscle: SpecificMuscle) -> SpecificMuscle:
        """
        Actualiza un músculo específico específico.
        """
        query = self.db.query(specific_muscle).filter(specific_muscle.id == id)
        result = query.first()
        result.name = specific_muscle.name
        self.db.commit()
        self.db.refresh(result)
        return result
    
    def get_specific_muscle_by_id(self, id: int) -> SpecificMuscle:
        """
        Obtiene un músculo específico específico.
        """
        query = self.db.query(specific_muscle).filter(specific_muscle.id == id)
        return query.first()
    
    