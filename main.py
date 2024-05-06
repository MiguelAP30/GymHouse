from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import incomes_router
from src.routers.egresos import egress_router
from src.routers.categoria_ingreso import categories_incomes_router
from src.routers.categoria_egreso import categories_egress_router
from src.routers.reportes import reportes_router
from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

##################################################
#                     Tags                       #

tags_metadata = [
    {"name": "incomes", "description": "imgresos"}, 
    { "name": "egress", "description": "egresos"}, 
    { "name": "reports", "description": "reportes"},  
    { "name": "categories_incomes", "description": "categorias de los ingresos"},
    { "name": "categories_egress", "description": "categorias de los egresos"},

    { "name": "users", "description": "usuarios"},
    { "name": "diet_users", "description": "dietas de los usuarios"},
    { "name": "diets", "description": "dietas"},
    { "name": "excercises_muscles_machines", "description": "ejercicios musculos maquinas"},
    { "name": "excercises", "description": "ejercicios"},
    { "name": "exercises_per_weeks_days", "description": "ejercicios por semanas dias"},
    { "name": "foods_categories", "description": "categorias de alimentos"},
    { "name": "foods", "description": "alimentos"},
    { "name": "machines", "description": "maquinas"},
    { "name": "meals", "description": "comidas"},
    { "name": "muscles", "description": "musculos"},
    { "name": "plates_per_weeks_days", "description": "platos por semanas dias"},
    { "name": "plates", "description": "platos"},
    { "name": "quantity_foods", "description": "cantidad de alimentos"},
    { "name": "roles", "description": "roles"},
    { "name": "tags_of_training_plans", "description": "etiquetas de los planes de entrenamiento"},
    { "name": "training_plans_exercises", "description": "planes de entrenamiento ejercicios"},
    { "name": "training_plans_users", "description": "planes de entrenamiento usuarios"},
    { "name": "training_plans", "description": "planes de entrenamiento"},
    { "name": "types_quantity", "description": "tipos de cantidad"},
    { "name": "week_days", "description": "dias de la semana"},
]

app = FastAPI(openapi_tags=tags_metadata)

#################################################
#                 Middlewares                   #

#app.add_middleware(ErrorHandler)

#################################################
#      Router's definition (endpoints sets)     #

app.include_router(router= incomes_router)
app.include_router(router= egress_router)
app.include_router(router= categories_incomes_router)
app.include_router(router= categories_egress_router)
app.include_router(prefix="/reports", router= reportes_router)

#################################################







