# Importaciones necesarias de FastAPI, tipado y estados HTTP
from fastapi import APIRouter
from typing import List
from starlette.status import HTTP_204_NO_CONTENT

# Esquemas que definen la estructura de los datos (entrada/salida)
from app.api.models.schemas.user import User, UserCount, UserResponse, UserCreate

# Servicios donde está la lógica de negocio para los usuarios
from app.api.db.repositories.users import (
    get_all_users,
    get_user_by_id,
    get_users_count,
    create_new_user,
    update_user_by_id,
    delete_user_by_id
)

# Se crea un enrutador específico para los endpoints de usuarios
user = APIRouter()

# Endpoint GET que devuelve todos los usuarios
@user.get("/", tags=["users"], response_model=List[UserResponse], description="Get a list of all users")
def get_users():
    return get_all_users()

# Endpoint GET que devuelve el número total de usuarios
@user.get("/count", tags=["users"], response_model=UserCount)
def count_users():
    return get_users_count()

# Endpoint GET que devuelve un usuario por ID
@user.get("/{id}", tags=["users"], response_model=UserResponse, description="Get a single user by Id")
def get_user(id: str):
    return get_user_by_id(id)

# Endpoint POST que crea un nuevo usuario
@user.post("/", tags=["users"], response_model=UserResponse, description="Create a new user")
def create_user(user: UserCreate):
    return create_new_user(user)

# Endpoint PUT que actualiza un usuario existente por su ID
@user.put("/{id}", tags=["users"], response_model=UserResponse, description="Update a User by Id")
def update_user(id: int, user: UserCreate):
    return update_user_by_id(id, user)

# Endpoint DELETE que elimina un usuario por su ID
@user.delete("/{id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
def delete_user(id: int):
    return delete_user_by_id(id)
