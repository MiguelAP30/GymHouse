from sqlalchemy import Column, ForeignKey, Integer, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class ExercisePerWeekDay(Base):
    __tablename__ = "exercises_per_week_days"

    id = Column(Integer, primary_key=True, autoincrement=True)
    week_day_id = Column(Integer, ForeignKey("week_days.id"))
    training_plan_exercise_id = Column(Integer, ForeignKey("training_plans_exercises.id"))

    week_days = relationship("WeekDay", back_populates="exercises_per_week_days")
    training_plans_exercises = relationship("TrainingPlanExercise", back_populates="exercises_per_week_days")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}