from typing import List
from src.models.star import Star as star
from src.schemas.star import Star

class StarRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase StarRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de StarRepository.
        """
        self.db = db
    
    def get_all_star(self) -> List[Star]:
        """
        Obtiene todas las estrellas.

        Returns:
            Una lista de objetos Star que representan las estrellas.

        Postcondición:
            - Se devuelve una lista de objetos Star.
        """
        query = self.db.query(star)
        return query.all()
    
    def create_new_star(self, star: Star) -> Star:
        """
        Crea una nueva estrella.

        Args:
            star: El objeto Star que representa la estrella a crear.

        Returns:
            El objeto Star creado.

        Precondición:
            - star debe ser un objeto Star válido.

        Postcondición:
            - Se crea una nueva estrella.
        """

        new_star = star(**star.model_dump())
        self.db.add(new_star)

        self.db.commit()
        self.db.refresh(new_star)
        return new_star
    
    def delete_star(self, id: int) -> dict:
        """
        Elimina una estrella específica.
        """
        query = self.db.query(star).filter(star.id == id)
        star = query.first()
        self.db.delete(star)
        self.db.commit()
        return {"message": "Star deleted successfully"}
    
    def update_star(self, id: int, star: Star) -> Star:
        """
        Actualiza una estrella específica.

        Args:
            id: El identificador de la estrella a actualizar.
            star: El objeto Star que representa la estrella a actualizar.

        Returns:
            El objeto Star actualizado.

        Precondición:
            - id debe ser un entero positivo.
            - star debe ser un objeto Star válido.

        Postcondición:
            - Se actualiza una estrella.
        """
        query = self.db.query(star).filter(star.id == id)
        star_db = query.first()
        star_db.name = star.name
        star_db.description = star.description
        self.db.commit()
        self.db.refresh(star_db)
        return star_db
    
    def get_star_by_id(self, id: int) -> Star:
        """
        Obtiene una estrella por su ID.

        Args:
            id: El ID de la estrella a obtener.

        Returns:
            El objeto Star que representa la estrella.

        Precondición:
            - id debe ser un entero positivo.

        Postcondición:
            - Se devuelve un objeto Star.
        """
        query = self.db.query(star).filter(star.id == id)
        return query.first()
    
    def get_star_by_training_plan_id(self, training_plan_id: int) -> List[Star]:
        """
        Obtiene todas las estrellas de un plan de entrenamiento específico.

        Args:
            training_plan_id: El ID del plan de entrenamiento.

        Returns:
            Una lista de objetos Star que representan las estrellas del plan de entrenamiento.

        Precondición:
            - training_plan_id debe ser un entero positivo.

        Postcondición:
            - Se devuelven las estrellas del plan de entrenamiento.
        """
        query = self.db.query(star).filter(star.training_plan_id == training_plan_id)
        return query.all()