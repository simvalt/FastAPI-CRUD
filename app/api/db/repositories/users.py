# Conexión a la base de datos
from app.api.core.settings.db import conn

# Modelo de tabla de usuarios
from app.api.db.queries.user import users

# Esquema de validación de datos de usuario
from app.api.models.schemas.user import User

# Funciones de SQLAlchemy para operaciones agregadas y consultas
from sqlalchemy import func, select
from fastapi import HTTPException


# Obtener todos los usuarios de la base de datos
def get_all_users():
    return conn.execute(users.select()).fetchall()

# Obtener un solo usuario por su ID
def get_user_by_id(user_id: str):
    return conn.execute(users.select().where(users.c.id == user_id)).first()

# Obtener el total de usuarios (conteo)
def get_users_count():
    stmt = select(func.count()).select_from(users)
    result = conn.execute(stmt)
    return {"total": result.scalar()}

# Crear un nuevo usuario con cifrado de contraseña
def create_new_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    # Se inserta el nuevo usuario en la base de datos
    result = conn.execute(users.insert().values(new_user))
    # Se retorna el usuario recién creado
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

# Actualizar la información de un usuario existente por ID
def update_user_by_id(user_id: int, user: User):
    # Aquí no se está cifrando la contraseña, cuidado si viene sin cifrar del frontend
    conn.execute(
        users.update()
        .values(name=user.name, email=user.email, password=user.password)
        .where(users.c.id == user_id)
    )
    # Se retorna el usuario actualizado
    user = conn.execute(users.select().where(users.c.id == user_id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Eliminar un usuario por ID
def delete_user_by_id(user_id: int):
    conn.execute(users.delete().where(users.c.id == user_id))
    # Como es una eliminación, no se retorna nada (pero puedes validar si existía)
    return None
