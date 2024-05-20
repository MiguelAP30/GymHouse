from fastapi import HTTPException, status 
from src.repositories.user import UserRepository 
from src.config.database import SessionLocal 
from src.auth import auth_handler 
from src.schemas.user import UserLogin as UserLoginSchema 
from src.schemas.user import User as UserCreateSchema

class AuthRepository:
    """
    Clase que representa el repositorio de autenticación.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia del repositorio de autenticación.
        """
        pass

    def register_user(self, user: UserCreateSchema) -> dict:
        """
        Registra un nuevo usuario en el sistema.

        Parámetros:
        - user: UserCreateSchema: Los datos del usuario a registrar.

        Precondición:
        - El usuario no debe existir en la base de datos.

        Postcondición:
        - Si el usuario se registra exitosamente, se devuelve un diccionario con los datos del usuario registrado.
        - Si el usuario ya existe, se lanza una excepción.

        Retorna:
        - dict: Un diccionario con los datos del usuario registrado.
        """
        db = SessionLocal()
        if UserRepository(db).get_user_by_email(email=user.email) is not None:
            raise Exception("La cuenta ya existe")
        hashed_password = auth_handler.hash_password(password=user.password)
        new_user: UserCreateSchema = UserCreateSchema(
            id_number=user.id_number,
            name=user.name,
            email=user.email,
            password=hashed_password,
            lastname=user.lastname,
            phone=user.phone,
            address=user.address,
            weight=user.weight,
            height=user.height,
            birth_date=user.birth_date,
            physical_activity=user.physical_activity,
            gender=user.gender,
            role_id=user.role_id,
        )
        return UserRepository(db).create_new_user(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:
        """
        Inicia sesión de un usuario en el sistema.

        Parámetros:
        - user: UserLoginSchema: Los datos del usuario para iniciar sesión.

        Precondición:
        - El usuario debe existir en la base de datos.

        Postcondición:
        - Si las credenciales son válidas, se devuelve un diccionario con el token de acceso y el token de actualización.
        - Si las credenciales son inválidas, se devuelve un objeto HTTPException con el código de estado 401.

        Retorna:
        - dict: Un diccionario con el token de acceso y el token de actualización.
        """
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
        access_token = auth_handler.encode_token(check_user)
        refresh_token = auth_handler.encode_refresh_token(check_user)
        return access_token, refresh_token