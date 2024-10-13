from sqlalchemy.orm import Session
from src.models.role import Role
from src.models.week_day import WeekDay
from src.models.muscle import Muscle
from src.models.specific_muscle import SpecificMuscle
from src.models.dificulty import Dificulty
from src.models.machine import Machine

def init_roles(db: Session):
    roles = [
        {"id": 1, "name": "Usuario Logueado", "description": "Rol de usuario logueado"},
        {"id": 2, "name": "Usuario Premium", "description": "Rol de usuario premium"},
        {"id": 3, "name": "Gym", "description": "Rol de gimnasio"},
        {"id": 4, "name": "Admin", "description": "Rol de administrador"}
    ]
    for role in roles:
        if not db.query(Role).filter_by(id=role["id"]).first():
            db.add(Role(**role))
    db.commit()

def init_week_days(db: Session):
    days = [
        {"id": 1, "name": "Lunes"},
        {"id": 2, "name": "Martes"},
        {"id": 3, "name": "Miércoles"},
        {"id": 4, "name": "Jueves"},
        {"id": 5, "name": "Viernes"},
        {"id": 6, "name": "Sábado"},
        {"id": 7, "name": "Domingo"}
    ]
    for day in days:
        if not db.query(WeekDay).filter_by(id=day["id"]).first():
            db.add(WeekDay(**day))
    db.commit()

def init_muscles(db: Session):
    muscles = [
        {"id": 1, "name": "Pecho", "description": "Grupo muscular en la parte delantera del torso, responsable de movimientos de empuje."},
        {"id": 2, "name": "Espalda", "description": "Grupo muscular en la parte posterior del torso, involucrado en movimientos de tracción y estabilización."},
        {"id": 3, "name": "Hombros", "description": "Grupo muscular ubicado en la parte superior del brazo, clave en movimientos de empuje y elevación."},
        {"id": 4, "name": "Brazos", "description": "Grupo muscular que incluye los músculos en la parte superior del brazo, responsable de flexión y extensión del codo."},
        {"id": 5, "name": "Antebrazos", "description": "Músculos responsables de la flexión y extensión de la muñeca y los dedos."},
        {"id": 6, "name": "Abdomen", "description": "Grupo muscular en la parte frontal del torso, fundamental para la estabilidad del core y movimientos de flexión del tronco."},
        {"id": 7, "name": "Zona Lumbar", "description": "Músculos en la parte baja de la espalda, esenciales para la estabilidad y extensión de la columna."},
        {"id": 8, "name": "Glúteos", "description": "Grupo muscular en la parte posterior de la cadera, involucrado en la extensión de la cadera y estabilización."},
        {"id": 9, "name": "Muslos", "description": "Grupo muscular en la parte frontal y posterior del muslo, responsable de la extensión y flexión de la rodilla."},
        {"id": 10, "name": "Aductores", "description": "Grupo muscular en la parte interna del muslo, encargado de la aducción de la pierna."},
        {"id": 11, "name": "Pantorrillas", "description": "Músculos en la parte inferior de la pierna, responsables de la flexión plantar del pie."},
        {"id": 12, "name": "Serrato Anterior", "description": "Músculo en la parte lateral del torso, involucrado en la estabilización de la escápula."},
        {"id": 13, "name": "Intercostales", "description": "Músculos entre las costillas, responsables de la expansión y contracción del tórax durante la respiración."},
        {"id": 14, "name": "Rotadores del Manguito Rotador", "description": "Grupo muscular responsable de la rotación y estabilidad del hombro."}
    ]
    for muscle in muscles:
        if not db.query(Muscle).filter_by(id=muscle["id"]).first():
            db.add(Muscle(**muscle))
    db.commit()

def init_specific_muscles(db: Session):
    specific_muscles = [
        {"id": 1, "name": "Pectoral Mayor", "muscle_id": 1, "description": "Músculo principal del pecho, responsable de la aducción y rotación interna del brazo."},
        {"id": 2, "name": "Pectoral Menor", "muscle_id": 1, "description": "Músculo pequeño bajo el pectoral mayor, responsable de la estabilización de la escápula."},
        {"id": 3, "name": "Trapecio", "muscle_id": 2, "description": "Músculo grande en la parte superior de la espalda, encargado de los movimientos de la escápula."},
        {"id": 4, "name": "Dorsal Ancho", "muscle_id": 2, "description": "Músculo principal de la espalda, responsable de la extensión y aducción del brazo."},
        {"id": 5, "name": "Deltoides Anterior", "muscle_id": 3, "description": "Parte frontal del músculo del hombro, involucrado en la flexión del brazo."},
        {"id": 6, "name": "Bíceps", "muscle_id": 4, "description": "Músculo en la parte frontal del brazo, encargado de la flexión del codo y la supinación del antebrazo."},
        {"id": 7, "name": "Tríceps", "muscle_id": 4, "description": "Músculo en la parte posterior del brazo, encargado de la extensión del codo."},
        {"id": 8, "name": "Flexores del Antebrazo", "muscle_id": 5, "description": "Músculos encargados de la flexión de la muñeca y los dedos."},
        {"id": 9, "name": "Extensores del Antebrazo", "muscle_id": 5, "description": "Músculos encargados de la extensión de la muñeca y los dedos."},
        {"id": 10, "name": "Recto Abdominal", "muscle_id": 6, "description": "Músculo frontal del abdomen, responsable de la flexión del tronco."},
        {"id": 11, "name": "Oblicuos Externos", "muscle_id": 6, "description": "Músculos laterales del abdomen, responsables de la rotación y flexión lateral del tronco."},
        {"id": 12, "name": "Erector de la Columna", "muscle_id": 7, "description": "Músculos largos a lo largo de la columna vertebral, encargados de su extensión y estabilidad."},
        {"id": 13, "name": "Glúteo Mayor", "muscle_id": 8, "description": "Músculo más grande de los glúteos, encargado de la extensión de la cadera."},
        {"id": 14, "name": "Cuádriceps", "muscle_id": 9, "description": "Grupo muscular en la parte frontal del muslo, responsable de la extensión de la rodilla."},
        {"id": 15, "name": "Isquiotibiales", "muscle_id": 9, "description": "Grupo muscular en la parte posterior del muslo, encargado de la flexión de la rodilla y extensión de la cadera."},
        {"id": 16, "name": "Aductor Mayor", "muscle_id": 10, "description": "Músculo principal en la parte interna del muslo, responsable de la aducción de la pierna."},
        {"id": 17, "name": "Gastrocnemio", "muscle_id": 11, "description": "Músculo grande en la pantorrilla, responsable de la flexión plantar del pie."},
        {"id": 18, "name": "Sóleo", "muscle_id": 11, "description": "Músculo profundo en la pantorrilla, que también contribuye a la flexión plantar del pie."},
        {"id": 19, "name": "Supraespinoso", "muscle_id": 14, "description": "Músculo del manguito rotador responsable de la abducción del brazo."}
    ]
    for specific_muscle in specific_muscles:
        if not db.query(SpecificMuscle).filter_by(id=specific_muscle["id"]).first():
            db.add(SpecificMuscle(**specific_muscle))
    db.commit()

def init_difficulties(db: Session):
    difficulties = [
        {"id": 1, "name": "Facil"},
        {"id": 2, "name": "Medio"},
        {"id": 3, "name": "Dificil"},
        {"id": 4, "name": "Experto"}
    ]
    for difficulty in difficulties:
        if not db.query(Dificulty).filter_by(id=difficulty["id"]).first():
            db.add(Dificulty(**difficulty))
    db.commit()

def init_machines(db: Session):
    machines = [
        {"id": 1, "name": "Barra Olímpica", "description": "Una barra de acero utilizada en levantamientos compuestos como sentadillas, peso muerto y press de banca. Es fundamental para entrenamientos de fuerza y levantamiento olímpico."},
        {"id": 2, "name": "Mancuernas", "description": "Pesos libres utilizados para entrenar de forma unilateral, lo que ayuda a equilibrar la fuerza entre ambos lados del cuerpo. Permiten una amplia variedad de ejercicios."},
        {"id": 3, "name": "Máquina de Fuerza", "description": "Dispositivos mecánicos que guían el movimiento y permiten entrenar músculos específicos de manera controlada y segura, reduciendo el riesgo de lesiones."},
        {"id": 4, "name": "Peso Corporal", "description": "Ejercicios que utilizan el peso del cuerpo como resistencia, como flexiones, sentadillas o dominadas, promoviendo fuerza funcional y estabilidad."},
        {"id": 5, "name": "Banda Elástica", "description": "Bandas de resistencia que añaden tensión progresiva a los movimientos. Ideales para entrenar músculos estabilizadores, rehabilitación y movilidad."},
        {"id": 6, "name": "Kettlebell", "description": "Pesas con forma de bola y una manija. Se utilizan para entrenamientos dinámicos que mejoran la fuerza, la potencia y la resistencia cardiovascular."},
        {"id": 7, "name": "Balón Medicinal", "description": "Pelotas pesadas que se usan para mejorar la potencia explosiva, la coordinación y la estabilidad del núcleo mediante ejercicios dinámicos."},
        {"id": 8, "name": "Cables", "description": "Sistema de poleas que permite movimientos multidireccionales y trabajar diferentes músculos. Ideal para entrenamientos funcionales y específicos."},
        {"id": 9, "name": "Caja Plyo", "description": "Plataforma elevada utilizada para ejercicios pliométricos como saltos, que mejoran la potencia explosiva, agilidad y coordinación."},
        {"id": 10, "name": "Banco", "description": "Superficie de apoyo para realizar ejercicios con mancuernas, barras u otros equipos. Es fundamental en ejercicios como press de banca y abdominales."},
        {"id": 11, "name": "Máquina Smith", "description": "Barra guiada que se mueve verticalmente, ideal para entrenar con mayor estabilidad y seguridad en ejercicios de fuerza como sentadillas y press de banca."},
        {"id": 12, "name": "Estiramientos", "description": "Herramientas o zonas diseñadas para realizar ejercicios de estiramiento que mejoran la flexibilidad y la movilidad, fundamentales para la recuperación."},
        {"id": 13, "name": "Cardio", "description": "Máquinas como bicicletas estáticas, cintas de correr y elípticas, usadas para mejorar la resistencia cardiovascular y quemar calorías."},
        {"id": 14, "name": "TRX", "description": "Sistema de suspensión que permite realizar ejercicios de peso corporal con énfasis en la estabilidad del núcleo y la fuerza funcional."},
        {"id": 15, "name": "Bosu Ball", "description": "Medio balón inflable utilizado para ejercicios de equilibrio, estabilidad y fortalecimiento del núcleo. Ideal para entrenamiento funcional."},
        {"id": 16, "name": "Recuperación", "description": "Máquinas y equipos utilizados para estiramientos, masajes y otros ejercicios enfocados en la recuperación muscular después del entrenamiento."},
        {"id": 17, "name": "Yoga", "description": "Espacios y accesorios como colchonetas y bloques utilizados para la práctica de yoga, mejorando la flexibilidad, equilibrio y relajación."},
        {"id": 18, "name": "Plato", "description": "Pesas circulares que se agregan a barras o se usan de manera independiente para aumentar la carga en levantamientos de fuerza."},
    ]
    for machine in machines:
        if not db.query(Machine).filter_by(id=machine["id"]).first():
            db.add(Machine(**machine))
    db.commit()

def init_data(db: Session):
    init_roles(db)
    init_week_days(db)
    init_muscles(db)
    init_specific_muscles(db)
    init_difficulties(db)
    init_machines(db)