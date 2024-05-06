from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class TrainingPlanUser(Base):
    __tablename__ = "training_plans_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    training_plan_id = Column(Integer, ForeignKey("training_plans.id"))
    user_email = Column(String, ForeignKey("users.email"))
    status = Column(Boolean, default=False)

    training_plans = relationship("TrainingPlan", back_populates="training_plans_users")
    users = relationship("User", back_populates="training_plans_users")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}