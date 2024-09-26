from typing import List
from src.models.dificulty import Dificulty as dificulty
from src.schemas.dificulty import Dificulty

class DificultyRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase DificultyRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de DificultyRepository.
        """
        self.db = db
    
    def get_all_dificulty(self) -> List[Dificulty]:
        """
        Obtiene todas las dificultades.

        Returns:
            Una lista de objetos Dificulty que representan las dificultades.

        Postcondición:
            - Se devuelve una lista de objetos Dificulty.
        """
        query = self.db.query(dificulty)
        return query.all()

    def create_new_dificulty(self, dificulty: Dificulty) -> Dificulty:
        """
        Crea una nueva dificultad.

        Args:
            dificulty: El objeto Dificulty que representa la dificultad a crear.

        Returns:
            El objeto Dificulty creado.

        Precondición:
            - dificulty debe ser un objeto Dificulty válido.

        Postcondición:
            - Se crea una nueva dificultad.
        """

        new_dificulty = dificulty(**dificulty.model_dump())
        self.db.add(new_dificulty)

        self.db.commit()
        self.db.refresh(new_dificulty)
        return new_dificulty
    
    def delete_dificulty(self, id: int) -> dict:
        """
        Elimina una dificultad específica.
        """
        element = self.db.query(dificulty).filter(dificulty.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element
    
    def update_dificulty(self, id: int, dificulty: Dificulty) -> Dificulty:
        """
        Actualiza una dificultad específica.
        """
        element = self.db.query(dificulty).filter(dificulty.id == id).first()
        element.name = dificulty.name
        element.description = dificulty.description
        self.db.commit()
        return element
    
    def get_dificulty_by_id(self, id: int) -> Dificulty:
        """
        Obtiene una dificultad específica por su ID.
        """
        element = self.db.query(dificulty).filter(dificulty.id == id).first()
        return element