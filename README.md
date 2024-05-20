# GymHouse

GymHouse es un proyecto diseñado para gestionar las necesidades de un gimnasio. Permite manejar usuarios, roles, ejercicios, músculos, máquinas, planes de entrenamiento, días de la semana, ejercicios detallados, alimentos, categorías de alimentos, tipos de cantidad, etiquetas de dietas y dietas.

## Instalación

Para instalar y ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:
```bash
git clone https://github.com/yourusername/gymhouse.git
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

## Endpoints

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
  /api/v1/diet: Gestión de dietas.
