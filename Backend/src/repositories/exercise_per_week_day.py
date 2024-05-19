from typing import List
from src.models.exercise_per_week_day import ExercisePerWeekDay as ExercisePerWeekDayModel
from src.models.week_day import WeekDay as WeekDayModel
from src.models.training_plan import TrainingPlan as TrainingPlanModel
from src.models.training_plan_user import TrainingPlanUser as TrainingPlanUserModel
from src.models.user import User as UserModel
from src.schemas.exercise_per_week_day import ExercisePerWeekDay


class ExercisePerWeekDayRepository:
    def __init__(self, db):
        self.db = db

    def get_all_my_excercise_per_week_day(self, user: str):
        exercises = self.db.query(ExercisePerWeekDayModel, WeekDayModel.name, TrainingPlanModel.name, UserModel.name).\
            join(TrainingPlanModel).\
            join(TrainingPlanUserModel).\
            join(WeekDayModel, ExercisePerWeekDayModel.week_day_id == WeekDayModel.id).\
            filter(TrainingPlanUserModel.user_email == user).\
            all()

        return self.group_exercises_by_day_and_training_plan(exercises)

    def get_premium_excercise_per_week_day(self):
        exercises = self.db.query(ExercisePerWeekDayModel, WeekDayModel.name, TrainingPlanModel.name, UserModel.name).\
            join(TrainingPlanModel).\
            join(TrainingPlanUserModel).\
            filter(TrainingPlanUserModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 2).\
            join(WeekDayModel, ExercisePerWeekDayModel.week_day_id == WeekDayModel.id).\
            all()

        return self.group_exercises_by_day_and_training_plan(exercises)

    def get_client_excercise_per_week_day(self):
        exercises = self.db.query(ExercisePerWeekDayModel, WeekDayModel.name, TrainingPlanModel.name, UserModel.name).\
            join(TrainingPlanModel).\
            join(TrainingPlanUserModel).\
            filter(TrainingPlanUserModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 3).\
            join(WeekDayModel, ExercisePerWeekDayModel.week_day_id == WeekDayModel.id).\
            all()

        return self.group_exercises_by_day_and_training_plan(exercises)

    def get_admin_excercise_per_week_day(self):
        exercises = self.db.query(ExercisePerWeekDayModel, WeekDayModel.name, TrainingPlanModel.name, UserModel.name).\
            join(TrainingPlanModel).\
            join(TrainingPlanUserModel).\
            filter(TrainingPlanUserModel.status == True).\
            join(UserModel).\
            filter(UserModel.role_id == 4).\
            join(WeekDayModel, ExercisePerWeekDayModel.week_day_id == WeekDayModel.id).\
            all()

        return self.group_exercises_by_day_and_training_plan(exercises)

    def group_exercises_by_day_and_training_plan(self, exercises):
        exercises_by_plan_and_day = {}
        for exercise, week_day_name, training_plan_name, user_name in exercises:
            if training_plan_name not in exercises_by_plan_and_day:
                exercises_by_plan_and_day[training_plan_name] = {
                    "created by": user_name,
                    "days": {}
                }
            if week_day_name not in exercises_by_plan_and_day[training_plan_name]["days"]:
                exercises_by_plan_and_day[training_plan_name]["days"][week_day_name] = []
            exercises_by_plan_and_day[training_plan_name]["days"][week_day_name].append(exercise)
        return exercises_by_plan_and_day

    def get_excercise_per_week_day_by_id(self, id, user: str):
        return self.db.query(ExercisePerWeekDayModel, WeekDayModel.name).join(WeekDayModel).filter(ExercisePerWeekDayModel.id == id, TrainingPlanUserModel.user_email == user).first()

    def create_new_excercise_per_week_day(self, exercise_per_week_day: ExercisePerWeekDay):
        new_excercise_per_week_day = ExercisePerWeekDayModel(**exercise_per_week_day.model_dump())

        self.db.add(new_excercise_per_week_day)
        self.db.commit()
        self.db.refresh(new_excercise_per_week_day)
        return new_excercise_per_week_day

    def delete_excercise_per_week_day(self, id, user: str):
        element = self.db.query(ExercisePerWeekDayModel).join(TrainingPlanModel).join(TrainingPlanUserModel).filter(ExercisePerWeekDayModel.id == id, TrainingPlanUserModel.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element