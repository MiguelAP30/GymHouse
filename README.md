# GymHouse

GymHouse es un proyecto diseñado para gestionar las necesidades de un gimnasio. Permite manejar usuarios, roles, ejercicios, músculos, máquinas, planes de entrenamiento, días de la semana, ejercicios detallados, alimentos, categorías de alimentos, tipos de cantidad, etiquetas de dietas y dietas.

## Instalación

Para instalar y ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:
```bash
git clone https://github.com/MiguelAP30/GymHouse.git
```
2. Navega al directorio del proyecto:
```bash
cd gymhouse
```
3. Instala las dependencias 
```bash
pip install -r requirements.txt
```
4. Ejecuta el servidor
```bash
uvicorn main:app --reload
```


## Endpoints CRUD

1. **Diet:**

   - Create Diet: /api/v1/diet/
   - Get All Diets: /api/v1/diet/
   - Get Diet By Id: /api/v1/diet/:id
   - Update Diet By Id: /api/v1/diet/:id
   - Delete Diet By Id: /api/v1/diet/:id

2. **Meal:**

   - Create Meal: /api/v1/meal/
   - Get All Meals: /api/v1/meal/
   - Get Meal By Id: /api/v1/meal/:id
   - Update Meal By Id: /api/v1/meal/:id
   - Delete Meal By Id: /api/v1/meal/:id

3. **Plate Per Week Day**

   - Create Plate Per Week Day: /api/v1/plate_per_week_day/
   - Get All My DIets: /api/v1/plate_per_week_day/my_diets
   - Get All Public Diets: /api/v1/plate_per_week_day/premium_diets
   - Get All Public Diets Users: /plate_per_week_day/client_diets
   - Get All Public Diets Professionals: /api/v1/plate_per_week_day/admin_diets
   - Get All Public Diets Administrative: /api/v1/plate_per_week_day/:id
   - Get Plate Per Week Day By id: /api/v1/plate_per_week_day/:id
   - Delete Plate Per Week Day By id: /api/v1/plate_per_week_day/:id
   
4. **Plate Per Week Day**

   - Get Alls Quantity Food: /api/v1/quantityFood/
   - Create Quantity Food: /api/v1/quantityFood/
   - Get Quantity Food By id: /api/v1/quantityFood/:id
   - Delete Quantity Food By id: /api/v1/quantityFood/:id
   - Update Quantity Food: /api/v1/quantityFood/:id

5. **Week Day**

   - Get Alls Week days: /api/v1/week_day/
   - Create Week Day: /api/v1/week_day/
   - Get Week Day By id: /api/v1/week_day/:id
   - Delete Week Day: /api/v1/week_day/:id
   - Update Week Day: /api/v1/week_day/:id

6. **Tag Training Plan**

   - Get Alls Tag Training Plans: /api/v1/tag_of_training_plan/
   - Create Tag Training Plan: /api/v1/tag_of_training_plan/
   - Get Tag Training Plan By id: /api/v1/tag_of_training_plan/:id
   - Delete Tag Training Plan By id: /api/v1/tag_of_training_plan/:id 
   - Update Tag Training Plan By id: /api/v1/tag_of_training_plan/:id

7. **Tag Diets**

   - Get Alls Tags Diets: /api/v1/tag_of_diet/
   - Create Tag Diet: /api/v1/tag_of_diet/
   - Get Tag Diet By id: /api/v1/tag_of_diet/:id
   - Delete Tag Diet By id: /api/v1/tag_of_diet/:id
   - Update Tag Diet By id: /api/v1/tag_of_diet/:id

8. **Type Quantity Food**

   - Get Alls Type Quantity Foods: /api/v1/type_quantity/
   - Create Quantity Food: /api/v1/type_quantity/
   - Get Quantity Food By id: /api/v1/type_quantity/:id
   - Delete Quantity Food By id: /api/v1/type_quantity/:id
   - Update Quantity Food By id: /api/v1/type_quantity/:id  

9. **Food Category**

   - Get Alls Food Categories: /api/v1/food_category/
   - Create Food Category: /api/v1/food_category/
   - Get Food Category By id: /api/v1/food_category/:id
   - Delete Food Category By id: /api/v1/food_category/:id
   - Update Food Category By id: /api/v1/food_category/:id

10. **Food**

   - Get Alls Foods: /api/v1/food/
   - Create Food: /api/v1/food/
   - Get Food By id: /api/v1/food/_id
   - Delete Food By id: /api/v1/food/:id
   - Update Food By id: /api/v1/food/:id

11. **Exercise**

   - Get Alls Exercises: /api/v1/exercise/
   - Create Exercise: /api/v1/exercise/
   - Get Exercises By id: /api/v1/exercise/:id
   - Delete Exercises By id: /api/v1/exercise/:id
   - Update Exercises By id: /api/v1/exercise/:id

12. **Muscle**

   - Get Alls Muscles: /api/v1/muscle/
   - Create Muscle: /api/v1/muscle/
   - Get Muscle By id: /api/v1/muscle/:id
   - Delete Muscle By id: /api/v1/muscle/:id
   - Update Muscle By id: /api/v1/muscle/:id

13. **Muscle**

   - Get Alls Machines: /api/v1/machine/
   - Create Machine: /api/v1/machine/
   - Get Machine By id: /api/v1/machine/:id
   - Delete Machine By id: /api/v1/machine/:id
   - Update Machine By id: /api/v1/machine/:id

14. **Exercise Muscle Machine**

   - Get Alls Exercise Muscle Machine By Rate: /api/v1/exercise_muscle_machine/exercises_by_rate?id=:id
   - Create Exercise Muscle Machine: /api/v1/exercise_muscle_machine/
   - Get Exercise Muscle Machine By Machine And Rate:/api/v1/exercise_muscle_machine/exercises_by_machine_and_rate?id_machine=:id&id_muscle=:id
   - Get Exercise Muscle Machine By id: /api/v1/exercise_muscle_machine/:id
   - Delete Exercise Muscle Machine By id: /api/v1/exercise_muscle_machine/:id
   - Update Exercise Muscle Machine By id: /api/v1/exercise_muscle_machine/:id

15. **Training Plan**

   - Get Alls Trainings Plans: /api/v1/training_plan/
   - Create Training Plan: /api/v1/training_plan/
   - Get Training Plan id: /api/v1/training_plan/:id
   - Detele Training Plan: /api/v1/training_plan/:id
   - Update Training Plan By Id: /api/v1/training_plan/:id

16. **Detailed Exercise**

   - Get Alls Detailed Exercises: /api/v1/detailed_exercise/
   - Create Detailed Exercise: /api/v1/detailed_exercise/
   - Get Detailed Exercise By id: /api/v1/detailed_exercise/:id
   - Update Detailed Exercise: /api/v1/detailed_exercise/:id
   - Delete Detailed Exercise: /api/v1/detailed_exercise/:id

17. **Exercise Per Week Day**

   - Get Alls My Exercises Per Week Day: /api/v1/exercise_per_week_day/my_exercises
   - Get Alls Premium Exercises Per Week Day: /api/v1/exercise_per_week_day/premium_exercises
   - Get Alls Client Exercises Per Week Day: /api/v1/exercise_per_week_day/client_exercises
   - Get Alls Admin Exercises Per Week Day: /api/v1/exercise_per_week_day/admin_exercises
   - Get Exercises Per Week Day By id: /api/v1/exercise_per_week_day/1
   - Delete Exercises Per Week Day By id: /api/v1/exercise_per_week_day/:id
   - Create Exercises Per Week Day: Create Exercises Per Week Day: /api/v1/exercise_per_week_day/

18. **Auth**

   - Register: /api/v1/register
   - Login: /api/v1/login
   - Refresh Token: /api/v1/refresh_token

19. **User**

   - Get All Users: /api/v1/user/
   - Get User By Email: /api/v1/user/:email
   - Deactive User: /api/v1/user/:email
   - Update User: /api/v1/user/:email
   - Update Role By Email: /api/v1/user/user_role/:email?role_id=:id

20. **Role**

   - Create Role: /api/v1/role/
   - Get all Roles: /api/v1/role/
   - Get Role By Id: /api/v1/role/:id
   - Upgrade Role: /api/v1/role/:id
   - Delete Role: /api/v1/role/:id