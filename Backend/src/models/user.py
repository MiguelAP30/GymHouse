from sqlalchemy import Column, ForeignKey, Integer, Float, Date, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String(length=250), primary_key=True)
    id_number = Column(String(length=20))
    password = Column(String(length=60))
    name = Column(String(length=50))
    lastname = Column(String(length=50))
    phone = Column(String(length=20))
    address = Column(String(length=150))
    weight = Column(Float)
    height = Column(Float)
    birth_date = Column(Date)
    physical_activity = Column(Integer)
    gender = Column(String(length=1))
    role_id = Column(Integer, ForeignKey("roles.id"))

    roles = relationship("Role", back_populates="users")
    diets = relationship("Diet", back_populates="users")
    training_plans = relationship("TrainingPlan", back_populates="users")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}