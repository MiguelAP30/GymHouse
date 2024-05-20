from typing import List
from src.schemas.tag_of_diet import TagOfDiet
from src.models.tag_of_diet import TagOfDiet as tag_of_diets

class TagOfDietRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_tag_of_diets(self) -> List[TagOfDiet]:
        """
        Obtiene todos los registros de etiquetas de dietas.
        
        Precondición:
        - No se requiere ninguna precondición.-
        
        Postcondición:
        - Devuelve una lista de objetos TagOfDiet que representan todas las etiquetas de dietas en la base de datos.
        """
        query = self.db.query(tag_of_diets)
        return query.all()
    
    def get_tag_of_diet_by_id(self, id: int ):
        """
        Obtiene una etiqueta de dieta por su ID.
        
        Precondición:
        - Se requiere un ID válido como parámetro.
        
        Postcondición:
        - Devuelve un objeto TagOfDiet que representa la etiqueta de dieta con el ID especificado.
        """
        element = self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        return element
    
    def delete_tag_of_diet(self, id: int ) -> dict:
        """
        Elimina una etiqueta de dieta por su ID.
        
        Precondición:
        - Se requiere un ID válido como parámetro.
        
        Postcondición:
        - Elimina la etiqueta de dieta con el ID especificado de la base de datos.
        - Devuelve un diccionario que representa la etiqueta de dieta eliminada.
        """
        element: TagOfDiet= self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_tag_of_diet(self, tag_of_diet:TagOfDiet ) -> dict:
        """
        Crea una nueva etiqueta de dieta.
        
        Precondición:
        - Se requiere un objeto TagOfDiet válido como parámetro.
        
        Postcondición:
        - Crea una nueva etiqueta de dieta en la base de datos.
        - Devuelve un diccionario que representa la nueva etiqueta de dieta creada.
        """
        new_tag_of_diet = tag_of_diets(**tag_of_diet.model_dump())
        self.db.add(new_tag_of_diet)
        
        self.db.commit()
        self.db.refresh(new_tag_of_diet)
        return new_tag_of_diet
    
    def update_tag_of_diet(self, id: int, tag_of_diet: TagOfDiet) -> dict:    
        """
        Actualiza una etiqueta de dieta por su ID.
        
        Precondición:
        - Se requiere un ID válido y un objeto TagOfDiet válido como parámetros.
        
        Postcondición:
        - Actualiza la etiqueta de dieta con el ID especificado en la base de datos.
        - Devuelve un diccionario que representa la etiqueta de dieta actualizada.
        """
        element = self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        element.name = tag_of_diet.name

        self.db.commit()
        self.db.refresh(element)
        return element