from typing import List
from src.schemas.quantityFood import QuantityFood
from src.models.quantityFood import QuantityFood as quantity_foods
from src.models.diet_user import DietUser as DietUserModel


class QuantityFoodRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase QuantityFoodRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se inicializa el objeto QuantityFoodRepository con la base de datos especificada.
        """
        self.db = db
    
    def get_all_quantity_foods(self, user:str) -> List[QuantityFood]:
        """
        Obtiene todos los alimentos en cantidad de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve una lista de objetos QuantityFood que representan los alimentos en cantidad.
        """
        query = self.db.query(quantity_foods).join(DietUserModel).filter(DietUserModel.user_email == user)
        return query.all()
    
    def get_quantity_food_by_id(self, id: int , user:str):
        """
        Obtiene un alimento en cantidad por su ID.

        Parámetros:
        - id: ID del alimento en cantidad.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve el objeto QuantityFood correspondiente al ID especificado.
        """
        element = self.db.query(quantity_foods).join(DietUserModel).filter(quantity_foods.id == id, DietUserModel.user_email == user).first()
        return element
    
    def delete_quantity_food(self, id: int, user: str) -> dict:
        """
        Elimina un alimento en cantidad de la base de datos.

        Parámetros:
        - id: ID del alimento en cantidad a eliminar.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - El alimento en cantidad correspondiente al ID especificado es eliminado de la base de datos.
        - Devuelve un diccionario que representa el alimento en cantidad eliminado.
        """
        element: QuantityFood= self.db.query(quantity_foods).join(DietUserModel).filter(quantity_foods.id == id, DietUserModel.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_quantity_food(self, quantity_food:QuantityFood ) -> dict:
        """
        Crea un nuevo alimento en cantidad en la base de datos.

        Parámetros:
        - quantity_food: objeto QuantityFood que representa el nuevo alimento en cantidad.

        Precondición:
        - quantity_food debe ser una instancia válida de la clase QuantityFood.

        Postcondición:
        - El nuevo alimento en cantidad es creado en la base de datos.
        - Devuelve un diccionario que representa el nuevo alimento en cantidad creado.
        """
        new_quantity_food = quantity_foods(**quantity_food.model_dump())
        self.db.add(new_quantity_food)
        
        self.db.commit()
        self.db.refresh(new_quantity_food)
        return new_quantity_food
    
    def update_quantity_food(self, id: int, quantity_food: QuantityFood) -> dict:
        """
        Actualiza un alimento en cantidad en la base de datos.

        Parámetros:
        - id: ID del alimento en cantidad a actualizar.
        - quantity_food: objeto QuantityFood que contiene los nuevos datos del alimento en cantidad.

        Precondición:
        - El ID debe ser un entero válido.
        - quantity_food debe ser una instancia válida de la clase QuantityFood.

        Postcondición:
        - El alimento en cantidad correspondiente al ID especificado es actualizado en la base de datos.
        - Devuelve un diccionario que representa el alimento en cantidad actualizado.
        """
        element = self.db.query(quantity_foods).filter(quantity_foods.id == id).first()
        element.value = quantity_food.value
        element.calorie = quantity_food.calorie
        element.protein = quantity_food.protein
        element.carbohydrate = quantity_food.carbohydrate
        element.fat = quantity_food.fat

        self.db.commit()
        self.db.refresh(element)
        return element