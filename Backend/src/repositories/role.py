from typing import List
from src.schemas.role import Role
from src.models.role import Role as roles

class RoleRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_roles(self) -> List[Role]:
        """
        Obtiene todos los roles almacenados en la base de datos.

        Precondición:
        - La base de datos debe estar conectada y disponible.

        Postcondición:
        - Devuelve una lista de objetos Role que representan todos los roles almacenados en la base de datos.
        """
        query = self.db.query(roles)
        return query.all()
    
    def get_role_by_id(self, id: int ):
        """
        Obtiene un rol específico por su ID.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve un objeto Role que representa el rol con el ID especificado.
        """
        element = self.db.query(roles).filter(roles.id == id).first()
        return element
    
    def delete_role(self, id: int ) -> dict:
        """
        Elimina un rol específico por su ID.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.

        Postcondición:
        - Elimina el rol con el ID especificado de la base de datos.
        - Devuelve un diccionario que contiene los datos del rol eliminado.
        """
        element: Role= self.db.query(roles).filter(roles.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_role(self, role:Role ) -> dict:
        """
        Crea un nuevo rol en la base de datos.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El parámetro role debe ser un objeto Role válido.

        Postcondición:
        - Crea un nuevo rol en la base de datos con los datos proporcionados.
        - Devuelve un diccionario que contiene los datos del nuevo rol creado.
        """
        new_role = roles(**role.model_dump())
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role
    
    def update_role(self, id: int, role: Role) -> dict:
        """
        Actualiza un rol existente en la base de datos.

        Precondición:
        - La base de datos debe estar conectada y disponible.
        - El ID debe ser un entero válido.
        - El parámetro role debe ser un objeto Role válido.

        Postcondición:
        - Actualiza el rol con el ID especificado en la base de datos con los datos proporcionados.
        - Devuelve un diccionario que contiene los datos del rol actualizado.
        """
        element = self.db.query(roles).filter(roles.id == id).first()
        element.name = role.name
        element.description = role.description
        self.db.commit()
        self.db.refresh(element)
        return element