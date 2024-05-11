from typing import List
from src.schemas.ingresos import Income
from src.models.ingreso import Ingreso as IngresoModel
from sqlalchemy import func

class IngresoRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_incomes(self) -> List[Income]: 
        query = self.db.query(IngresoModel)
        return query.all()
    
    def get_ingreso_by_id(self, id: int ):
        element = self.db.query(IngresoModel).filter(IngresoModel.id == id).first()    
        return element

    def delete_ingreso(self, id: int ) -> dict: 
        element: Income= self.db.query(IngresoModel).filter(IngresoModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_ingreso(self, income:Income ) -> dict:
        new_income = IngresoModel(**income.model_dump())    
        self.db.add(new_income)
        self.db.commit()    
        self.db.refresh(new_income)
        return new_income

    def suma_all_incomes(self) -> float: 
        total = self.db.query(func.sum(IngresoModel.value)).scalar()
        return total or 0.0
    
    def get_ingresos_by_category(self, category:int) -> List[Income]:
        query = self.db.query(IngresoModel).filter(IngresoModel.categoria == category)
        return query.all()