from typing import List
from src.schemas.diet import Diet
from src.models.diet import Diet as diets

class DietRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_diets(self) -> List[Diet]:
        """
        Obtiene todas las dietas almacenadas en la base de datos.

        Precondición:
        - La base de datos debe estar conectada y disponible.

        Postcondición:
        - Devuelve una lista de objetos de tipo Diet que representan todas las dietas almacenadas en la base de datos.
        """
        query = self.db.query(diets)
        return query.all()
    
    def get_diet_by_id(self, id: int ):
        """
        Obtiene una dieta específica por su ID.

        Parámetros:
        - id: El ID de la dieta a obtener.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve un objeto de tipo Diet que representa la dieta encontrada.
        """
        element = self.db.query(diets).filter(diets.id == id).first()
        return element
    
    def delete_diet(self, id: int ) -> dict:
        """
        Elimina una dieta específica por su ID.

        Parámetros:
        - id: El ID de la dieta a eliminar.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.

        Postcondición:
        - Elimina la dieta de la base de datos y devuelve un diccionario que contiene los datos de la dieta eliminada.
        """
        element: Diet= self.db.query(diets).filter(diets.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_diet(self, diet:Diet ) -> dict:
        """
        Crea una nueva dieta en la base de datos.

        Parámetros:
        - diet: Objeto de tipo Diet que representa la dieta a crear.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El objeto diet debe ser una instancia válida de la clase Diet.

        Postcondición:
        - Crea una nueva dieta en la base de datos y devuelve un diccionario que contiene los datos de la nueva dieta creada.
        """
        new_diet = diets(**diet.model_dump())
        self.db.add(new_diet)
        
        self.db.commit()
        self.db.refresh(new_diet)
        return new_diet
    
    def update_diet(self, id: int, diet: Diet) -> dict:
        """
        Actualiza una dieta existente en la base de datos.

        Parámetros:
        - id: El ID de la dieta a actualizar.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.
        - El objeto diet debe ser una instancia válida de la clase Diet.

        Postcondición:
        - Actualiza la dieta en la base de datos y devuelve un diccionario que contiene los datos de la dieta actualizada.
        """
        element = self.db.query(diets).filter(diets.id == id).first()
        element.name = diet.name
        element.description = diet.description
        element.tag_of_diet_id = diet.tags_of_diet_id

        self.db.commit()
        self.db.refresh(element)
        return element