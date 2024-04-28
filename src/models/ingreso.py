from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Ingreso(Base):    
    __tablename__ = "ingresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)    
    fecha           = Column(Date)    
    descripcion     = Column(String(length=150))   
    valor           = Column(Integer)   
    categoria_id    = Column(Integer, ForeignKey("categorias_ingresos.id"))

    categoria = relationship("Categoria_Ingreso", back_populates="ingresos")