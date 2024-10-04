from fastapi import HTTPException, status 
from src.repositories.user import UserRepository 
from src.config.database import SessionLocal 
from src.auth import auth_handler 
from src.schemas.user import UserLogin as UserLoginSchema 
from src.schemas.user import User as UserCreateSchema

class AuthRepository:
    def __init__(self) -> None:
        pass

    def register_user(self, user: UserCreateSchema) -> dict:
        db = SessionLocal()
        if UserRepository(db).get_user_by_email(email=user.email) is not None:
            raise Exception("La cuenta ya existe")
        hashed_password = auth_handler.hash_password(password=user.password)
        new_user: UserCreateSchema = UserCreateSchema(
            email=user.email,
            id_number=user.id_number,
            password=hashed_password,
            user_name=user.user_name,
            name=user.name,
            phone=user.phone,
            address=user.address,
            birth_date=user.birth_date,
            gender=user.gender,
        )
        return UserRepository(db).create_new_user(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:
        db = SessionLocal()
        check_user = UserRepository(db).get_user_by_email(email=user.email)
        if check_user is None:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas (1)",
            )
        if not auth_handler.verify_password(user.password, check_user.password):
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas (2)",
            )
        if not check_user.status:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Cuenta deshabilitada",
            )
        access_token = auth_handler.encode_token(check_user)
        refresh_token = auth_handler.encode_refresh_token(check_user)
        return access_token, refresh_token