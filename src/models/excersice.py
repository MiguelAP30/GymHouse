from sqlalchemy import Column, ForeignKey, Integer, String, Date, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    description = Column(String(length=150))
    video = Column(String(length=150))
    image = Column(String(length=150))
    dateAdded = Column(Date)

    exercises_muscles_machines = relationship("ExerciseMuscleMachine", back_populates="exercises")
    training_plans_exercises = relationship("TrainingPlanExercise", back_populates="exercises")
    exercises_per_week_days = relationship("ExercisePerWeekDay", back_populates="exercises")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}