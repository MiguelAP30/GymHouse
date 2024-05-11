from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import incomes_router
from src.routers.egresos import egress_router
from src.routers.categoria_ingreso import categories_incomes_router
from src.routers.categoria_egreso import categories_egress_router
from src.routers.reportes import reportes_router

from src.routers.diet_meal import diet_meal_router
from src.routers.diet_user import diet_user_router
from src.routers.diet import diet_router
from src.routers.exercise_muscle_machine import exercise_muscle_machine_router
from src.routers.exercise_per_week_day import exercise_per_week_day_router
from src.routers.exercise import exercise_router
from src.routers.food_category import food_category_router
from src.routers.food import food_router
from src.routers.machine import machine_router
from src.routers.meal import meal_router
from src.routers.muscle import muscle_router
from src.routers.plate_per_week_day import plate_per_week_day_router
from src.routers.quantityFood import quantityFood_router
from src.routers.role import role_router
from src.routers.tag_of_training_plan import tag_of_training_plan_router
from src.routers.training_plan_exercise import training_plan_exercise_router
from src.routers.training_plan_user import training_plan_user_router
from src.routers.training_plan import training_plan_router
from src.routers.type_quantity import type_quantity_router
from src.routers.user import user_router
from src.routers.week_day import week_day_router

from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

##################################################
#                     Tags                       #

tags_metadata = []


app = FastAPI(openapi_tags=tags_metadata)

#################################################
#                 Middlewares                   #

app.add_middleware(ErrorHandler)

#################################################
#      Router's definition (endpoints sets)     #

app.include_router(router= incomes_router)
app.include_router(router= egress_router)
app.include_router(router= categories_incomes_router)
app.include_router(router= categories_egress_router)
app.include_router(prefix="/reports", router= reportes_router)
app.include_router(prefix="/diet_meal", router= diet_meal_router)
app.include_router(prefix="/diet_user", router= diet_user_router)
app.include_router(prefix="/diet", router= diet_router)
app.include_router(prefix="/exercise_muscle_machine", router= exercise_muscle_machine_router)
app.include_router(prefix="/exercise_per_week_day", router= exercise_per_week_day_router)
app.include_router(prefix="/exercise", router= exercise_router)
app.include_router(prefix="/food_category", router= food_category_router)
app.include_router(prefix="/food", router= food_router)
app.include_router(prefix="/machine", router= machine_router)
app.include_router(prefix="/meal", router= meal_router)
app.include_router(prefix="/muscle", router= muscle_router)
app.include_router(prefix="/plate_per_week_day", router= plate_per_week_day_router)
app.include_router(prefix="/quantityFood", router= quantityFood_router)
app.include_router(prefix="/role", router= role_router)
app.include_router(prefix="/tag_of_training_plan", router= tag_of_training_plan_router)
app.include_router(prefix="/training_plan_exercise", router= training_plan_exercise_router)
app.include_router(prefix="/training_plan_user", router= training_plan_user_router)
app.include_router(prefix="/training_plan", router= training_plan_router)
app.include_router(prefix="/type_quantity", router= type_quantity_router)
app.include_router(prefix="/user", router= user_router)
app.include_router(prefix="/week_day", router= week_day_router)



#################################################







