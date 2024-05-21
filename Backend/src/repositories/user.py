from typing import List
from src.schemas.user import User
from src.models.user import User as users

class UserRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de UserRepository.

        Args:
            db: La conexión a la base de datos.

        Precondición:
            - db debe ser una conexión válida a la base de datos.

        Postcondición:
            - Se crea una nueva instancia de UserRepository.
        """
        self.db = db
    
    def get_all_users(self) -> List[User]:
        """
        Obtiene todos los usuarios de la base de datos.

        Returns:
            Una lista de objetos User que representan a todos los usuarios en la base de datos.

        Precondición:
            - No se requiere ninguna precondición.

        Postcondición:
            - Se devuelve una lista de objetos User que representan a todos los usuarios en la base de datos.
        """
        query = self.db.query(users)
        return query.all()
    
    def get_user_by_id(self, id: str ):
        """
        Obtiene un usuario de la base de datos por su ID.

        Args:
            id: El ID del usuario a buscar.

        Returns:
            El objeto User que representa al usuario encontrado, o None si no se encuentra ningún usuario con el ID dado.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se devuelve el objeto User que representa al usuario encontrado, o None si no se encuentra ningún usuario con el ID dado.
        """
        element = self.db.query(users).filter(users.id_number == id).first()
        return element
    
    def get_user_by_email(self, email: str):
        """
        Obtiene un usuario de la base de datos por su dirección de correo electrónico.

        Args:
            email: La dirección de correo electrónico del usuario a buscar.

        Returns:
            El objeto User que representa al usuario encontrado, o None si no se encuentra ningún usuario con el correo electrónico dado.

        Precondición:
            - email debe ser una cadena de caracteres válida.

        Postcondición:
            - Se devuelve el objeto User que representa al usuario encontrado, o None si no se encuentra ningún usuario con el correo electrónico dado.
        """
        element = self.db.query(users).filter(users.email == email).first()
        return element
    
    def delete_user(self, email: str ) -> dict:
        """
        Desactiva un usuario de la base de datos por su dirección de correo electrónico.

        Args:
            email: La dirección de correo electrónico del usuario a eliminar.

        Returns:
            Un diccionario que contiene la información del usuario eliminado.

        Precondición:
            - email debe ser una cadena de caracteres válida.

        Postcondición:
            - Se cambia el estado del usuario en la base de datos y se devuelve un diccionario que contiene su información.
        """
        element: User= self.db.query(users).filter(users.email == email).first()
        element.status = False
        self.db.commit()
        self.db.refresh(element)
        return element

    def create_new_user(self, user:User ) -> dict:
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            user: El objeto User que representa al usuario a crear.

        Returns:
            Un diccionario que contiene la información del usuario creado.

        Precondición:
            - user debe ser un objeto User válido.

        Postcondición:
            - Se crea un nuevo usuario en la base de datos y se devuelve un diccionario que contiene su información.
        """
        new_user = users(**user.model_dump())
        self.db.add(new_user)
        
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, email: str, user: User) -> dict:
        """
        Actualiza la información de un usuario en la base de datos.

        Args:
            email: La dirección de correo electrónico del usuario a actualizar.
            user: El objeto User que contiene la nueva información del usuario.

        Returns:
            Un diccionario que contiene la información del usuario actualizado.

        Precondición:
            - email debe ser una cadena de caracteres válida.
            - user debe ser un objeto User válido.

        Postcondición:
            - Se actualiza la información del usuario en la base de datos y se devuelve un diccionario que contiene su información actualizada.
        """
        element = self.db.query(users).filter(users.email == email).first()
        element.id_number = user.id_number
        element.password = user.password
        element.name = user.name
        element.lastname = user.lastname
        element.address = user.address
        element.phone = user.phone
        element.weight = user.weight
        element.height = user.height
        element.birth_date = user.birth_date
        element.physical_activity = user.physical_activity

        self.db.commit()
        self.db.refresh(element)
        return element

    def update_role(self, email: str, role_id: int) -> dict:
        """
        Actualiza el rol de un usuario en la base de datos.

        Args:
            email: La dirección de correo electrónico del usuario a actualizar.
            role_id: El ID del nuevo rol del usuario.

        Returns:
            Un diccionario que contiene la información del usuario actualizado.

        Precondición:
            - email debe ser una cadena de caracteres válida.
            - role_id debe ser un entero válido.

        Postcondición:
            - Se actualiza el rol del usuario en la base de datos y se devuelve un diccionario que contiene su información actualizada.
        """
        element = self.db.query(users).filter(users.email == email).first()
        element.role_id = role_id
        self.db.commit()
        self.db.refresh(element)
        return element
