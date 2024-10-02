from sqlalchemy.orm import Session
from src.models.role import Role
from src.models.week_day import WeekDay
from src.models.muscle import Muscle
from src.models.specific_muscle import SpecificMuscle
from src.models.dificulty import Dificulty

def init_roles(db: Session):
    roles = [
        {"id": 1, "name": "Admin", "description": "Role de administrador"},
        {"id": 2, "name": "User", "description": "Role de usuario"},
        {"id": 3, "name": "Trainer", "description": "Role de entrenador"},
        {"id": 4, "name": "Guest", "description": "Role de invitado"}
    ]
    for role in roles:
        if not db.query(Role).filter_by(id=role["id"]).first():
            db.add(Role(**role))
    db.commit()

def init_week_days(db: Session):
    days = [
        {"id": 1, "name": "Monday"},
        {"id": 2, "name": "Tuesday"},
        {"id": 3, "name": "Wednesday"},
        {"id": 4, "name": "Thursday"},
        {"id": 5, "name": "Friday"},
        {"id": 6, "name": "Saturday"},
        {"id": 7, "name": "Sunday"}
    ]
    for day in days:
        if not db.query(WeekDay).filter_by(id=day["id"]).first():
            db.add(WeekDay(**day))
    db.commit()

def init_muscles(db: Session):
    muscles = [
        {"id": 1, "name": "Chest", "description": "Músculo en la parte delantera del tórax"},
        {"id": 2, "name": "Back", "description": "Músculo grande en la parte posterior del torso"},
        {"id": 3, "name": "Legs", "description": "Músculo en la parte frontal del muslo"}
    ]
    for muscle in muscles:
        if not db.query(Muscle).filter_by(id=muscle["id"]).first():
            db.add(Muscle(**muscle))
    db.commit()

def init_specific_muscles(db: Session):
    specific_muscles = [
        {"id": 1, "name": "Biceps", "muscle_id": 1, "description": "Músculo en la parte frontal del brazo"},
        {"id": 2, "name": "Triceps", "muscle_id": 1, "description": "Músculo en la parte posterior del brazo"},
        {"id": 3, "name": "Quadriceps", "muscle_id": 3, "description": "Músculo en la parte frontal del muslo"}
    ]
    for specific_muscle in specific_muscles:
        if not db.query(SpecificMuscle).filter_by(id=specific_muscle["id"]).first():
            db.add(SpecificMuscle(**specific_muscle))
    db.commit()

def init_difficulties(db: Session):
    difficulties = [
        {"id": 1, "name": "Easy"},
        {"id": 2, "name": "Medium"},
        {"id": 3, "name": "Hard"},
        {"id": 4, "name": "Extreme"}
    ]
    for difficulty in difficulties:
        if not db.query(Dificulty).filter_by(id=difficulty["id"]).first():
            db.add(Dificulty(**difficulty))
    db.commit()

def init_data(db: Session):
    init_roles(db)
    init_week_days(db)
    init_muscles(db)
    init_specific_muscles(db)
    init_difficulties(db)