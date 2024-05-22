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

## Endpoints generales

  1. /api/v1/auth: Autenticación de usuarios.
  2. /api/v1/user: Gestión de usuarios.
  3. /api/v1/role: Gestión de roles.
  4. /api/v1/exercise: Gestión de ejercicios.
  5. /api/v1/muscle: Gestión de músculos.
  6. /api/v1/machine: Gestión de máquinas.
  7. /api/v1/exercise_muscle_machine: Gestión de ejercicios, músculos y máquinas.
  8. /api/v1/tag_of_training_plan: Gestión de etiquetas de planes de entrenamiento.
  9. /api/v1/training_plan: Gestión de planes de entrenamiento.
  10. /api/v1/week_day: Gestión de días de la semana.
  11. /api/v1/detailed_exercise: Gestión de ejercicios detallados.
  12. /api/v1/exercise_per_week_day: Gestión de ejercicios por día de la semana.
  13. /api/v1/food_category: Gestión de categorías de alimentos.
  14. /api/v1/type_quantity: Gestión de tipos de cantidad.
  15. /api/v1/food: Gestión de alimentos.
  16. /api/v1/tag_of_diet: Gestión de etiquetas de dietas.

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