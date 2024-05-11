from typing import List
from src.models.exercise_per_week_day import ExercisePerWeekDay as ExercisePerWeekDayModel
from src.schemas.exercise_per_week_day import ExercisePerWeekDay

class ExercisePerWeekDayRepository:
    def __init__(self, db):
        self.db = db

    def get_all_excercise_per_week_day(self):
        return self.db.query(ExercisePerWeekDayModel).all()

    def get_excercise_per_week_day_by_id(self, id):
        return self.db.query(ExercisePerWeekDayModel).filter(ExercisePerWeekDayModel.id == id).first()

    def create_new_excercise_per_week_day(self, exercise_per_week_day: ExercisePerWeekDay):
        new_excercise_per_week_day = ExercisePerWeekDayModel(**exercise_per_week_day.model_dump())

        self.db.add(new_excercise_per_week_day)
        self.db.commit()
        self.db.refresh(new_excercise_per_week_day)
        return new_excercise_per_week_day

    def delete_excercise_per_week_day(self, id):
        element = self.db.query(ExercisePerWeekDayModel).filter(ExercisePerWeekDayModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element
    