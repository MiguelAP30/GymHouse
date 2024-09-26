from typing import List
from src.models.profile import Profile as profiles
from src.schemas.profile import Profile

class ProfileRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase ProfileRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de ProfileRepository.
        """
        self.db = db

    def get_all_profile(self) -> List[Profile]:
        """
        Obtiene todos los perfiles.

        Returns:
            Una lista de objetos Profile que representan los perfiles.

        Postcondición:
            - Se devuelve una lista de objetos Profile.
        """
        elements = self.db.query(profiles)
        return elements.all()
    
    def create_new_profile(self, profile: Profile) -> Profile:
        """
        Crea un nuevo perfil.

        Args:
            profile: El objeto Profile que representa el perfil a crear.

        Returns:
            El objeto Profile creado.

        Precondición:
            - profile debe ser un objeto Profile válido.

        Postcondición:
            - Se crea un nuevo perfil.
        """

        new_profile = profiles(**profile.model_dump())
        self.db.add(new_profile)

        self.db.commit()
        self.db.refresh(new_profile)
        return new_profile
    
    def delete_profile(self, id: int) -> dict:
        """
        Elimina un perfil específico.
        """
        element: Profile= self.db.query(profiles).filter(profiles.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element 

    
    def update_profile(self, id: int, profile: Profile) -> Profile:
        """
        Actualiza un perfil específico.

        Args:
            id: El identificador del perfil a actualizar.
            profile: El objeto Profile que representa el perfil a actualizar.

        Returns:
            El objeto Profile actualizado.

        Precondición:
            - id debe ser un entero positivo.
            - profile debe ser un objeto Profile válido.

        Postcondición:
            - Se actualiza un perfil.
        """
        element = self.db.query(profiles).filter(profiles.id == id).first()
        element.name = profile.name
        element.description = profile.description
        self.db.commit()
        self.db.refresh(element)
        return element
    
    def get_profile_by_id(self, id: int) -> Profile:
        """
        Obtiene un perfil específico.

        Args:
            id: El identificador del perfil a obtener.

        Returns:
            El objeto Profile que representa el perfil.

        Precondición:
            - id debe ser un entero positivo.

        Postcondición:
            - Se devuelve un objeto Profile.
        """
        element = self.db.query(profiles).filter(profiles.id == id).first()
        return element