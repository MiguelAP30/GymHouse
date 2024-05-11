from typing import List
from src.schemas.machine import Machine
from src.models.machine import Machine as machines

class MachineRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_machines(self) -> List[Machine]:
        query = self.db.query(machines)
        return query.all()
    
    def get_machine_by_id(self, id: int ):
        element = self.db.query(machines).filter(machines.id == id).first()
        return element
    
    def delete_machine(self, id: int ) -> dict:
        element: Machine= self.db.query(machines).filter(machines.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_machine(self, machine:Machine ) -> dict:
        new_machine = machines(**machine.model_dump())
        self.db.add(new_machine)
        
        self.db.commit()
        self.db.refresh(new_machine)
        return new_machine
    
    def update_machine(self, id: int, machine: Machine) -> dict:
        element = self.db.query(machines).filter(machines.id == id).first()
        element.name = machine.name
        element.description = machine.description

        self.db.commit()
        self.db.refresh(element)
        return element