from fastapi import APIRouter
from app.api.routes.user import user

router = APIRouter()

router.include_router(user, tags=["users"], prefix="/user")
