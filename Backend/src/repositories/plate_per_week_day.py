from typing import List
from src.schemas.plate_per_week_day import PlatePerWeekDay
from src.models.plate_per_week_day import PlatePerWeekDay as plate_per_week_days
from src.models.week_day import WeekDay as WeekDayModel
from src.models.diet import Diet as DietModel
from src.models.user import User as UserModel
from src.models.meal import Meal as MealModel
from src.models.diet import Diet as DietModel


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

    def group_meals_by_day_and_diet(self, meals):
        """
        Agrupa las comidas por día de la semana y dieta.

        Parámetros:
        - meals: lista de comidas por día de la semana.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve un diccionario que agrupa las comidas por día de la semana y dieta.
        """
        meals_by_day_and_diet = {}
        for meal, week_day_name, diet_name, user_name in meals:
            if week_day_name not in meals_by_day_and_diet:
                meals_by_day_and_diet[week_day_name] = {
                    "created_by": user_name,
                    "diets": {}
                }
            if diet_name not in meals_by_day_and_diet[week_day_name]["diets"]:
                meals_by_day_and_diet[week_day_name]["diets"][diet_name] = []
            meals_by_day_and_diet[week_day_name]["diets"][diet_name].append(meal)
        return meals_by_day_and_diet

    def get_all_my_plate_per_week_day(self, user: str) -> List[PlatePerWeekDay]:
        """
        Obtiene todos los platos por día de la semana para un usuario específico.

        Parámetros:
        - user: correo electrónico del usuario.

        Precondición:
        - El usuario debe existir en la base de datos.

        Postcondición:
        - Devuelve una lista de objetos PlatePerWeekDay que representan los platos por día de la semana.
        """
        plates = self.db.query(plate_per_week_days, WeekDayModel.name, DietModel.name, UserModel.name).\
            join(DietModel).\
            join(DietModel).\
            join(WeekDayModel, plate_per_week_days.week_day_id == WeekDayModel.id).\
            filter(DietModel.user_email == user).\
            all()

        return self.group_meals_by_day_and_diet(plates)
    
    def get_all_premium_plate_per_week_day(self) -> List[PlatePerWeekDay]:
        """
        Obtiene todos los platos por día de la semana para usuarios premium.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve un diccionario que agrupa los platos por día de la semana y dieta.
        """
        plates = self.db.query(plate_per_week_days, WeekDayModel.name, DietModel.name, UserModel.name).\
            join(DietModel).\
            join(DietModel).\
            filter(DietModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 2).\
            join(WeekDayModel, plate_per_week_days.week_day_id == WeekDayModel.id).\
            all()

        return self.group_meals_by_day_and_diet(plates)
    
    def get_all_client_plate_per_week_day(self) -> List[PlatePerWeekDay]:
        """
        Obtiene todos los platos por día de la semana para usuarios clientes.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve un diccionario que agrupa los platos por día de la semana y dieta.
        """
        plates = self.db.query(plate_per_week_days, WeekDayModel.name, DietModel.name, UserModel.name).\
            join(DietModel).\
            join(DietModel).\
            filter(DietModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 3).\
            join(WeekDayModel, plate_per_week_days.week_day_id == WeekDayModel.id).\
            all()

        return self.group_meals_by_day_and_diet(plates)
    
    def get_admin_plate_per_week_day(self) -> List[PlatePerWeekDay]:
        """
        Obtiene todos los platos por día de la semana para usuarios administradores.

        Precondición:
        - Ninguna.

        Postcondición:
        - Devuelve un diccionario que agrupa los platos por día de la semana y dieta.
        """
        plates = self.db.query(plate_per_week_days, WeekDayModel.name, DietModel.name, UserModel.name).\
            join(DietModel).\
            join(DietModel).\
            filter(DietModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 4).\
            join(WeekDayModel, plate_per_week_days.week_day_id == WeekDayModel.id).\
            all()

        return self.group_meals_by_day_and_diet(plates)
    
    def get_plate_per_week_day_by_id(self, id: int, user:str) -> PlatePerWeekDay:
        """
        Obtiene un plato por día de la semana por su ID.

        Parámetros:
        - id: ID del plato por día de la semana.

        Precondición:
        - El ID debe ser un entero válido.

        Postcondición:
        - Devuelve el objeto PlatePerWeekDay correspondiente al ID proporcionado.
        """
        return self.db.query(plate_per_week_days, WeekDayModel.name).join(WeekDayModel).filter(plate_per_week_days.id == id, DietModel.user_email == user).first()
    
    def delete_plate_per_week_day(self, id: int, user:str ) -> dict:
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
        element: PlatePerWeekDay= self.db.query(plate_per_week_days).join(DietModel).join(DietModel).filter(plate_per_week_days.id == id, DietModel.user_email == user).first()
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