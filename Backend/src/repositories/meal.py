from typing import List
from src.schemas.meal import Meal
from src.models.meal import Meal as meals

class MealRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una instancia de MealRepository.

        Args:
            db: La base de datos utilizada para almacenar las comidas.
        """
        self.db = db
    
    def get_all_meals(self) -> List[Meal]:
        """
        Obtiene todas las comidas almacenadas en la base de datos.

        Returns:
            Una lista de objetos Meal que representan todas las comidas almacenadas.
        """
        query = self.db.query(meals)
        return query.all()
    
    def get_meal_by_id(self, id: int ):
        """
        Obtiene una comida específica por su ID.

        Args:
            id: El ID de la comida a obtener.

        Returns:
            El objeto Meal correspondiente al ID proporcionado.
        """
        element = self.db.query(meals).filter(meals.id == id).first()
        return element
    
    def delete_meal(self, id: int ) -> dict:
        """
        Elimina una comida de la base de datos.

        Args:
            id: El ID de la comida a eliminar.

        Returns:
            Un diccionario que contiene la información de la comida eliminada.
        """
        element: Meal= self.db.query(meals).filter(meals.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_meal(self, meal:Meal ) -> dict:
        """
        Crea una nueva comida y la guarda en la base de datos.

        Args:
            meal: El objeto Meal que representa la nueva comida a crear.

        Returns:
            Un diccionario que contiene la información de la nueva comida creada.
        """
        new_meal = meals(**meal.model_dump())
        self.db.add(new_meal)
        
        self.db.commit()
        self.db.refresh(new_meal)
        return new_meal
    
    def update_meal(self, id:int, meal:Meal ) -> dict:
        """
        Actualiza una comida existente en la base de datos.

        Args:
            id: El ID de la comida a actualizar.
            meal: El objeto Meal que contiene los nuevos datos de la comida.

        Returns:
            Un diccionario que contiene la información de la comida actualizada.
        """
        element = self.db.query(meals).filter(meals.id == id).first()
        element.name = meal.name
        element.description = meal.description
        self.db.commit()
        return element
    