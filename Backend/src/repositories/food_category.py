from typing import List
from src.schemas.food_category import FoodCategory
from src.models.food_category import FoodCategory as FoodCategoryModel

class FoodCategoryRepository:
    def __init__(self, db):
        """
        Inicializa una instancia de la clase FoodCategoryRepository.

        parametros:
            db: Objeto de la base de datos.

        Precondición:
            - db debe ser un objeto válido de la base de datos.

        Postcondición:
            - Se inicializa una instancia de la clase FoodCategoryRepository.
        """
        self.db = db

    def get_all_food_categories(self):
        """
        Obtiene todas las categorías de alimentos.

        Precondición:
            - No hay precondiciones.

        Postcondición:
            - Devuelve una lista con todas las categorías de alimentos.
        """
        return self.db.query(FoodCategoryModel).all()

    def get_food_category_by_id(self, id):
        """
        Obtiene una categoría de alimento por su ID.

        parametros:
            id: ID de la categoría de alimento.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Devuelve la categoría de alimento correspondiente al ID proporcionado.
        """
        return self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()

    def create_new_food_category(self, food_category: FoodCategory):
        """
        Crea una nueva categoría de alimento.

        parametros:
            food_category: Objeto de la categoría de alimento.

        Precondición:
            - food_category debe ser un objeto válido de la categoría de alimento.

        Postcondición:
            - Se crea una nueva categoría de alimento en la base de datos y se devuelve el objeto creado.
        """
        new_food_category = FoodCategoryModel(**food_category.model_dump())

        self.db.add(new_food_category)
        self.db.commit()
        self.db.refresh(new_food_category)
        return new_food_category

    def delete_food_category(self, id):
        """
        Elimina una categoría de alimento por su ID.

        parametros:
            id: ID de la categoría de alimento.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se elimina la categoría de alimento correspondiente al ID proporcionado de la base de datos y se devuelve el objeto eliminado.
        """
        element = self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()

        self.db.delete(element)
        self.db.commit()
        return element
    
    def update_food_category(self, id: int, food_category: FoodCategory) -> dict:
        """
        Actualiza una categoría de alimento por su ID.

        parametros:
            id: ID de la categoría de alimento.
            food_category: Objeto de la categoría de alimento actualizada.

        Precondición:
            - id debe ser un entero válido.
            - food_category debe ser un objeto válido de la categoría de alimento.

        Postcondición:
            - Se actualiza la categoría de alimento correspondiente al ID proporcionado en la base de datos y se devuelve el objeto actualizado.
        """
        element = self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()
        element.name = food_category.name

        self.db.commit()
        self.db.refresh(element)
        return element
