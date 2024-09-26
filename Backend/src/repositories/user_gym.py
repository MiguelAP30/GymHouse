from typing import List
from src.models.user_gym import UserGym as user_gym
from src.schemas.user_gym import UserGym

class UserGymRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase UserGymRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de UserGymRepository.
        """
        self.db = db

    def get_all_user_gym(self, current_user) -> List[UserGym]:
        """
        Obtiene todos los usuarios de un gimnasio.

        Returns:
            Una lista de objetos UserGym que representan los usuarios de un gimnasio.

        Postcondición:
            - Se devuelve una lista de objetos UserGym.
        """
        query = self.db.query(user_gym).filter(user_gym.gym_id == current_user)
        return query.all()
    
    def create_new_user_gym(self, user_gym: UserGym) -> UserGym:
        """
        Crea un nuevo usuario de un gimnasio.

        Args:
            user_gym: El objeto UserGym que representa el usuario de un gimnasio a crear.

        Returns:
            El objeto UserGym creado.

        Precondición:
            - user_gym debe ser un objeto UserGym válido.

        Postcondición:
            - Se crea un nuevo usuario de un gimnasio.
        """

        new_user_gym = user_gym(**user_gym.model_dump())
        self.db.add(new_user_gym)

        self.db.commit()
        self.db.refresh(new_user_gym)
        return new_user_gym
    
    def delete_user_gym(self, id: int) -> dict:
        """
        Elimina un usuario de un gimnasio específico.

        Args:
            id: El ID del usuario de un gimnasio a eliminar.

        Returns:
            Un diccionario con un mensaje de confirmación.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se elimina un usuario de un gimnasio.
        """
        element = self.db.query(user_gym).filter(user_gym.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return {"message": "The user_gym was successfully deleted", "data": None}
    
    def update_user_gym(self, id: int, user_gym: UserGym) -> UserGym:
        """
        Actualiza un usuario de un gimnasio específico.

        Args:
            id: El ID del usuario de un gimnasio a actualizar.
            user_gym: El objeto UserGym que representa el usuario de un gimnasio a actualizar.

        Returns:
            El objeto UserGym actualizado.

        Precondición:
            - id debe ser un entero válido.
            - user_gym debe ser un objeto UserGym válido.

        Postcondición:
            - Se actualiza un usuario de un gimnasio.
        """
        element = self.db.query(user_gym).filter(user_gym.id == id).first()
        for var, value in user_gym.model_dump().items():
            setattr(element, var, value)
        self.db.commit()
        self.db.refresh(element)
        return element
    
    def get_user_gym_by_id(self, id: int) -> UserGym:
        """
        Obtiene un usuario de un gimnasio específico.

        Args:
            id: El ID del usuario de un gimnasio a obtener.

        Returns:
            El objeto UserGym solicitado.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se devuelve un usuario de un gimnasio.
        """
        element = self.db.query(user_gym).filter(user_gym.id == id).first()
        return element
    
    def get_user_gym_by_user_id(self, user_id: int) -> UserGym:
        """
        Obtiene un usuario de un gimnasio específico.

        Args:
            user_id: El ID del usuario a obtener.

        Returns:
            El objeto UserGym solicitado.

        Precondición:
            - user_id debe ser un entero válido.

        Postcondición:
            - Se devuelve un usuario de un gimnasio.
        """
        element = self.db.query(user_gym).filter(user_gym.user_id == user_id).first()
        return element