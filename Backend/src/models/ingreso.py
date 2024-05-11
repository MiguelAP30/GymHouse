from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, inspect
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Ingreso(Base):    
    __tablename__ = "ingresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)    
    fecha           = Column(Date)    
    description     = Column(String(length=150))   
    value           = Column(Float)   
    categoria       = Column(Integer, ForeignKey("categorias_ingresos.id"))

    categoria_ingreso = relationship("Categoria_Ingreso", back_populates="ingresos")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}