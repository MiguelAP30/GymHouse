from sqlalchemy import Column, ForeignKey, Integer, String, Float, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class TrainingPlanExercise(Base):
    __tablename__ = "training_plans_exercises"

    id = Column(Integer, primary_key=True, autoincrement=True)
    training_plan_id = Column(Integer, ForeignKey("training_plans.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    sets = Column(Integer)
    reps = Column(Integer)
    rest = Column(Float)

    training_plans = relationship("TrainingPlan", back_populates="training_plans_exercises")
    exercises = relationship("Exercise", back_populates="training_plans_exercises")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}