from typing import List
from src.schemas.type_quantity import TypeQuantity
from src.models.type_quantity import TypeQuantity as type_quantities

class TypeQuantityRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase TypeQuantityRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se crea una instancia de TypeQuantityRepository con el objeto de la base de datos asignado.
        """
        self.db = db
    
    def get_all_type_quantities(self) -> List[TypeQuantity]:
        """
        Obtiene todas las instancias de TypeQuantity de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve una lista de todas las instancias de TypeQuantity en la base de datos.
        """
        query = self.db.query(type_quantities)
        return query.all()
    
    def get_type_quantity_by_id(self, id: int ):
        """
        Obtiene una instancia de TypeQuantity por su ID.

        Parámetros:
        - id: ID de la instancia de TypeQuantity a obtener.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve la instancia de TypeQuantity correspondiente al ID proporcionado.
        """
        element = self.db.query(type_quantities).filter(type_quantities.id == id).first()
        return element
    
    def delete_type_quantity(self, id: int ) -> dict:
        """
        Elimina una instancia de TypeQuantity de la base de datos.

        Parámetros:
        - id: ID de la instancia de TypeQuantity a eliminar.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - La instancia de TypeQuantity correspondiente al ID proporcionado es eliminada de la base de datos.
        - Devuelve un diccionario con los datos de la instancia eliminada.
        """
        element: TypeQuantity= self.db.query(type_quantities).filter(type_quantities.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_type_quantity(self, type_quantity:TypeQuantity ) -> dict:
        """
        Crea una nueva instancia de TypeQuantity en la base de datos.

        Parámetros:
        - type_quantity: objeto TypeQuantity a crear.

        Precondición:
        - type_quantity debe ser una instancia válida de TypeQuantity.

        Postcondición:
        - Se crea una nueva instancia de TypeQuantity en la base de datos.
        - Devuelve un diccionario con los datos de la nueva instancia creada.
        """
        new_type_quantity = type_quantities(**type_quantity.model_dump())
        self.db.add(new_type_quantity)
        
        self.db.commit()
        self.db.refresh(new_type_quantity)
        return new_type_quantity
    
    def update_type_quantity(self, id: int, type_quantity: TypeQuantity) -> dict:
        """
        Actualiza una instancia de TypeQuantity en la base de datos.

        Parámetros:
        - id: ID de la instancia de TypeQuantity a actualizar.
        - type_quantity: objeto TypeQuantity con los nuevos datos.

        Precondición:
        - El ID debe ser un entero válido.
        - type_quantity debe ser una instancia válida de TypeQuantity.

        Postcondición:
        - La instancia de TypeQuantity correspondiente al ID proporcionado es actualizada en la base de datos.
        - Devuelve un diccionario con los datos de la instancia actualizada.
        """
        element = self.db.query(type_quantities).filter(type_quantities.id == id).first()
        element.name = type_quantity.name
        element.description = type_quantity.description

        self.db.commit()
        self.db.refresh(element)
        return element