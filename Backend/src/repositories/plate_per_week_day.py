from typing import List
from src.schemas.plate_per_week_day import PlatePerWeekDay
from src.models.plate_per_week_day import PlatePerWeekDay as plate_per_week_days

class PlatePerWeekDayRepository():
    def __init__(self, db) -> None:
        """
        Constructor de la clase PlatePerWeekDayRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - Ninguna.

        Postcondición:
        - Se crea una instancia de la clase PlatePerWeekDayRepository.
        """
        self.db = db
    
    def get_all_plate_per_week_days(self) -> List[PlatePerWeekDay]:
        """
        Obtiene todos los platos por día de la semana.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve una lista de objetos PlatePerWeekDay que representan los platos por día de la semana.
        """
        query = self.db.query(plate_per_week_days)
        return query.all()
    
    def get_plate_per_week_day_by_id(self, id: int ):
        """
        Obtiene un plato por día de la semana por su ID.

        Parámetros:
        - id: ID del plato por día de la semana.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve el objeto PlatePerWeekDay correspondiente al ID proporcionado.
        """
        element = self.db.query(plate_per_week_days).filter(plate_per_week_days.id == id).first()
        return element
    
    def delete_plate_per_week_day(self, id: int ) -> dict:
        """
        Elimina un plato por día de la semana por su ID.

        Parámetros:
        - id: ID del plato por día de la semana.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - Elimina el objeto PlatePerWeekDay correspondiente al ID proporcionado de la base de datos.
        - Devuelve el objeto PlatePerWeekDay eliminado.
        """
        element: PlatePerWeekDay= self.db.query(plate_per_week_days).filter(plate_per_week_days.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_plate_per_week_day(self, plate_per_week_day:PlatePerWeekDay ) -> dict:
        """
        Crea un nuevo plato por día de la semana.

        Parámetros:
        - plate_per_week_day: objeto PlatePerWeekDay que representa el nuevo plato por día de la semana.

        Precondición:
        - plate_per_week_day debe ser un objeto válido de la clase PlatePerWeekDay.

        Postcondición:
        - Crea un nuevo objeto PlatePerWeekDay en la base de datos.
        - Devuelve el objeto PlatePerWeekDay creado.
        """
        new_plate_per_week_day = plate_per_week_days(**plate_per_week_day.model_dump())
        self.db.add(new_plate_per_week_day)
        
        self.db.commit()
        self.db.refresh(new_plate_per_week_day)
        return new_plate_per_week_day