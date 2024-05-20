from typing import List
from src.models.exercise import Exercise as ExerciseModel
from src.schemas.exercise import Exercise

class ExerciseRepository:
    def __init__(self, db):
        """
        Constructor de la clase ExerciseRepository.

        Parámetros:
        - db: objeto de la base de datos.

        Precondición:
        - db debe ser un objeto válido de la base de datos.

        Postcondición:
        - Se inicializa el objeto ExerciseRepository con la base de datos especificada.
        """
        self.db = db

    def get_all_excercises(self):
        """
        Obtiene todos los ejercicios de la base de datos.

        Precondición:
        - No hay precondiciones.

        Postcondición:
        - Devuelve una lista con todos los ejercicios de la base de datos.
        """
        return self.db.query(ExerciseModel).all()

    def get_excercise_by_id(self, id):
        """
        Obtiene un ejercicio de la base de datos por su ID.

        Parámetros:
        - id: ID del ejercicio a buscar.

        Precondición:
        - id debe ser un valor válido de ID.

        Postcondición:
        - Devuelve el ejercicio correspondiente al ID especificado.
        """
        return self.db.query(ExerciseModel).filter(ExerciseModel.id == id).first()

    def create_new_excercise(self, exercise: Exercise):
        """
        Crea un nuevo ejercicio en la base de datos.

        Parámetros:
        - exercise: objeto de tipo Exercise que representa el ejercicio a crear.

        Precondición:
        - exercise debe ser un objeto válido de tipo Exercise.

        Postcondición:
        - Crea un nuevo ejercicio en la base de datos y lo devuelve.
        """
        new_excercise = ExerciseModel(**exercise.model_dump())

        self.db.add(new_excercise)
        self.db.commit()
        self.db.refresh(new_excercise)
        return new_excercise

    def delete_excercise(self, id):
        """
        Elimina un ejercicio de la base de datos por su ID.

        Parámetros:
        - id: ID del ejercicio a eliminar.

        Precondición:
        - id debe ser un valor válido de ID.

        Postcondición:
        - Elimina el ejercicio correspondiente al ID especificado y lo devuelve.
        """
        element = self.db.query(ExerciseModel).filter(ExerciseModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element
    
    def update_excercise(self, id: int, exercise: Exercise) -> dict:
        """
        Actualiza un ejercicio en la base de datos por su ID.

        Parámetros:
        - id: ID del ejercicio a actualizar.
        - exercise: objeto de tipo Exercise que representa los nuevos datos del ejercicio.

        Precondición:
        - id debe ser un valor válido de ID.
        - exercise debe ser un objeto válido de tipo Exercise.

        Postcondición:
        - Actualiza el ejercicio correspondiente al ID especificado con los nuevos datos y lo devuelve.
        """
        element = self.db.query(ExerciseModel).filter(ExerciseModel.id == id).first()
        element.name = exercise.name
        element.description = exercise.description
        element.image = exercise.image
        element.video = exercise.video
        element.dateAdded = exercise.dateAdded

        self.db.commit()
        self.db.refresh(element)
        return element