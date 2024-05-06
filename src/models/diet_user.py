from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class DietUser(Base):
    __tablename__ = "diets_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    diet_id = Column(Integer, ForeignKey("diets.id"))
    user_email = Column(String, ForeignKey("users.email"))

    diets = relationship("Diet", back_populates="diets_users")
    users = relationship("User", back_populates="diets_users")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}