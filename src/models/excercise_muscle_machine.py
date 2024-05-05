from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class ExerciseMuscleMachine(Base):
    __tablename__ = "exercises_muscles_machines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    muscle_id = Column(Integer, ForeignKey("muscles.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"))
    rate = Column(Integer)

    exercises = relationship("Exercise", back_populates="exercises_muscles_machines")
    muscles = relationship("Muscle", back_populates="exercises_muscles_machines")
    machines = relationship("Machine", back_populates="exercises_muscles_machines")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}