from typing import List
from src.schemas.week_day import WeekDay
from src.models.week_day import WeekDay as week_days

class WeekDayRepository():
    def __init__(self, db) -> None:
        """
        Inicializa una nueva instancia de la clase WeekDayRepository.

        Args:
            db: La base de datos utilizada para realizar las operaciones.

        Precondición:
            - db debe ser una instancia válida de la base de datos.

        Postcondición:
            - Se crea una nueva instancia de WeekDayRepository.
        """
        self.db = db
    
    def get_all_week_days(self) -> List[WeekDay]:
        """
        Obtiene todos los días de la semana.

        Returns:
            Una lista de objetos WeekDay que representan los días de la semana.

        Postcondición:
            - Se devuelve una lista de objetos WeekDay.
        """
        query = self.db.query(week_days)
        return query.all()
    
    def get_week_day_by_id(self, id: int ):
        """
        Obtiene un día de la semana por su ID.

        Args:
            id: El ID del día de la semana a buscar.

        Returns:
            El objeto WeekDay correspondiente al ID proporcionado.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se devuelve el objeto WeekDay correspondiente al ID proporcionado.
        """
        element = self.db.query(week_days).filter(week_days.id == id).first()
        return element
    
    def delete_week_day(self, id: int ) -> dict:
        """
        Elimina un día de la semana por su ID.

        Args:
            id: El ID del día de la semana a eliminar.

        Returns:
            Un diccionario que contiene la información del día de la semana eliminado.

        Precondición:
            - id debe ser un entero válido.

        Postcondición:
            - Se elimina el día de la semana correspondiente al ID proporcionado.
            - Se devuelve un diccionario con la información del día de la semana eliminado.
        """
        element: WeekDay= self.db.query(week_days).filter(week_days.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_week_day(self, week_day:WeekDay ) -> dict:
        """
        Crea un nuevo día de la semana.

        Args:
            week_day: El objeto WeekDay que representa el nuevo día de la semana.

        Returns:
            Un diccionario que contiene la información del nuevo día de la semana creado.

        Precondición:
            - week_day debe ser un objeto válido de la clase WeekDay.

        Postcondición:
            - Se crea un nuevo día de la semana con la información proporcionada.
            - Se devuelve un diccionario con la información del nuevo día de la semana creado.
        """
        new_week_day = week_days(**week_day.model_dump())
        self.db.add(new_week_day)
        
        self.db.commit()
        self.db.refresh(new_week_day)
        return new_week_day
    
    def update_week_day(self, id: int, week_day: WeekDay) -> dict:
        """
        Actualiza un día de la semana por su ID.

        Args:
            id: El ID del día de la semana a actualizar.
            week_day: El objeto WeekDay que contiene la nueva información del día de la semana.

        Returns:
            Un diccionario que contiene la información del día de la semana actualizado.

        Precondición:
            - id debe ser un entero válido.
            - week_day debe ser un objeto válido de la clase WeekDay.

        Postcondición:
            - Se actualiza el día de la semana correspondiente al ID proporcionado con la nueva información.
            - Se devuelve un diccionario con la información del día de la semana actualizado.
        """
        element = self.db.query(week_days).filter(week_days.id == id).first()
        element.name = week_day.name

        self.db.commit()
        self.db.refresh(element)
        return element
    
    def get_week_day_by_name(self, name: str):
        """
        Obtiene un día de la semana por su nombre.

        Args:
            name: El nombre del día de la semana a buscar.

        Returns:
            El objeto WeekDay correspondiente al nombre proporcionado.

        Precondición:
            - name debe ser una cadena de caracteres válida.

        Postcondición:
            - Se devuelve el objeto WeekDay correspondiente al nombre proporcionado.
        """
        element = self.db.query(week_days).filter(week_days.name == name).first()
        return element