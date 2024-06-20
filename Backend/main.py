from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler

from src.routers.exercise_muscle_machine import exercise_muscle_machine_router
from src.routers.exercise_per_week_day import exercise_per_week_day_router
from src.routers.exercise import exercise_router
from src.routers.machine import machine_router
from src.routers.muscle import muscle_router
from src.routers.role import role_router
from src.routers.tag_of_training_plan import tag_of_training_plan_router
from src.routers.detailed_exercise import detailed_exercise_router
from src.routers.training_plan import training_plan_router
from src.routers.user import user_router
from src.routers.week_day import week_day_router
from src.routers.auth import auth_router

from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

##################################################
#                     Tags                       #

API_VERSION = 1

tags_metadata = []


#################################################

app = FastAPI(openapi_tags=tags_metadata, root_path=f"/api/v{API_VERSION}")


#################################################
#                 Middlewares                   #

#app.add_middleware(ErrorHandler)

#################################################
#      Router's definition (endpoints sets)     #

app.include_router(router=auth_router)
app.include_router(prefix="/user", router= user_router)
app.include_router(prefix="/role", router= role_router)
app.include_router(prefix="/exercise", router= exercise_router)
app.include_router(prefix="/muscle", router= muscle_router)
app.include_router(prefix="/machine", router= machine_router)
app.include_router(prefix="/exercise_muscle_machine", router= exercise_muscle_machine_router)
app.include_router(prefix="/tag_of_training_plan", router= tag_of_training_plan_router)
app.include_router(prefix="/training_plan", router= training_plan_router)
app.include_router(prefix="/week_day", router= week_day_router)
app.include_router(prefix="/detailed_exercise", router= detailed_exercise_router)
app.include_router(prefix="/exercise_per_week_day", router= exercise_per_week_day_router)


#################################################







