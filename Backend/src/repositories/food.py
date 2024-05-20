from typing import List
from src.schemas.food import Food
from src.models.food import Food as foods

class FoodRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una instancia de la clase FoodRepository.

        Args:
            db: La conexión a la base de datos.

        Precondición:
            - db es una conexión válida a la base de datos.

        Postcondición:
            - Se crea una instancia de FoodRepository con la conexión a la base de datos asignada.
        """
        self.db = db
    
    def get_all_foods(self) -> List[Food]:
        """
        Obtiene todos los alimentos de la base de datos.

        Precondición:
            - No se requiere ninguna precondición.

        Postcondición:
            - Devuelve una lista de objetos Food que representan todos los alimentos en la base de datos.
        """
        query = self.db.query(foods)
        return query.all()
    
    def get_food_by_id(self, id: int ):
        """
        Obtiene un alimento de la base de datos por su ID.

        Args:
            id: El ID del alimento a buscar.

        Precondición:
            - id es un entero válido.

        Postcondición:
            - Devuelve el objeto Food correspondiente al ID proporcionado.
        """
        element = self.db.query(foods).filter(foods.id == id).first()
        return element
    
    def delete_food(self, id: int ) -> dict:
        """
        Elimina un alimento de la base de datos por su ID.

        Args:
            id: El ID del alimento a eliminar.

        Precondición:
            - id es un entero válido.

        Postcondición:
            - El alimento correspondiente al ID proporcionado se elimina de la base de datos.
            - Devuelve un diccionario que contiene los datos del alimento eliminado.
        """
        element: Food= self.db.query(foods).filter(foods.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_food(self, food:Food ) -> dict:
        """
        Crea un nuevo alimento en la base de datos.

        Args:
            food: El objeto Food que representa el nuevo alimento a crear.

        Precondición:
            - food es un objeto Food válido.

        Postcondición:
            - Se crea un nuevo alimento en la base de datos con los datos proporcionados.
            - Devuelve un diccionario que contiene los datos del nuevo alimento creado.
        """
        new_food = foods(**food.model_dump())
        self.db.add(new_food)
        
        self.db.commit()
        self.db.refresh(new_food)
        return new_food
    
    def update_food(self, id: int, food: Food) -> dict:
        """
        Actualiza un alimento en la base de datos por su ID.

        Args:
            id: El ID del alimento a actualizar.
            food: El objeto Food que contiene los nuevos datos del alimento.

        Precondición:
            - id es un entero válido.
            - food es un objeto Food válido.

        Postcondición:
            - El alimento correspondiente al ID proporcionado se actualiza con los nuevos datos.
            - Devuelve un diccionario que contiene los datos del alimento actualizado.
        """
        element = self.db.query(foods).filter(foods.id == id).first()
        element.name = food.name
        element.description = food.description
        element.image = food.image

        self.db.commit()
        self.db.refresh(element)
        return element