from typing import List
from src.schemas.diet_user import DietUser
from src.models.diet_user import DietUser as diet_users

class DietUserRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase DietUserRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se inicializa el objeto DietUserRepository con el objeto de la base de datos.
        """
        self.db = db
    
    def get_all_diet_user(self) -> List[DietUser]:
        """
        Obtiene todos los usuarios de dieta.

        Parámetros:
        - Ninguno.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve una lista de objetos DietUser que representan a todos los usuarios de dieta en la base de datos.
        """
        query = self.db.query(diet_users)
        return query.all()
    
    def get_diet_user_by_id(self, id: int ):
        """
        Obtiene un usuario de dieta por su ID.

        Parámetros:
        - id: ID del usuario de dieta a buscar.

        Precondición:
        - El parámetro id debe ser un entero.

        Postcondición:
        - Devuelve el objeto DietUser que corresponde al ID proporcionado.
        """
        element = self.db.query(diet_users).filter(diet_users.id == id).first()
        return element
    
    def delete_diet_user(self, id: int ) -> dict:
        """
        Elimina un usuario de dieta por su ID.

        Parámetros:
        - id: ID del usuario de dieta a eliminar.

        Precondición:
        - El parámetro id debe ser un entero.

        Postcondición:
        - Elimina el usuario de dieta correspondiente al ID proporcionado de la base de datos.
        - Devuelve un diccionario que representa al usuario de dieta eliminado.
        """
        element: DietUser= self.db.query(diet_users).filter(diet_users.id == id).first()
        self.db.delete(element)

        self.db.commit()
        self.db.refresh(element)
        return element

    def create_new_diet_user(self, diet_user:DietUser ) -> dict:
        """
        Crea un nuevo usuario de dieta.

        Parámetros:
        - diet_user: objeto DietUser que representa al nuevo usuario de dieta a crear.

        Precondición:
        - El parámetro diet_user debe ser un objeto de la clase DietUser.

        Postcondición:
        - Crea un nuevo usuario de dieta en la base de datos con los datos proporcionados.
        - Devuelve un diccionario que representa al nuevo usuario de dieta creado.
        """
        new_diet_user = diet_users(**diet_user.model_dump())
        self.db.add(new_diet_user)
        
        self.db.commit()
        self.db.refresh(new_diet_user)
        return new_diet_user
    