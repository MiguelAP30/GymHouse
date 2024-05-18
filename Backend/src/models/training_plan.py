from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class TrainingPlan(Base):
    __tablename__ = "training_plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=60))
    description = Column(String(length=200))
    tag_of_training_plan_id = Column(Integer, ForeignKey("tags_of_training_plans.id"))
    exercise_per_week_day_id = Column(Integer, ForeignKey("exercises_per_week_days.id"))

    exercises_per_week_days = relationship("ExercisePerWeekDay", back_populates="training_plans")
    tags_of_training_plans = relationship("TagOfTrainingPlan", back_populates="training_plans")
    training_plans_users = relationship("TrainingPlanUser", back_populates="training_plans")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}