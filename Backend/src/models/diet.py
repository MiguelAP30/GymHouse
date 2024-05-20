from sqlalchemy import Column, ForeignKey, Integer, String, inspect, Boolean    
from sqlalchemy.orm import relationship
from src.config.database import Base

class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    description = Column(String(length=200))
    tags_of_diet_id = Column(Integer, ForeignKey("tags_of_diets.id"))
    user_email = Column(String(length=200), ForeignKey("users.email"))
    is_active = Column(Boolean, default=False)

    plates_per_weeks_days = relationship("PlatePerWeekDay", back_populates="diets")
    tags_of_diets = relationship("TagOfDiet", back_populates="diets")
    users = relationship("User", back_populates="diets")
    

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}