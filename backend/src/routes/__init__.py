from fastapi import APIRouter
from src.routes import auth_routes, user_routes

router = APIRouter()

router.include_router(auth_routes.router, tags=["auth"], prefix="/auth")
router.include_router(user_routes.router, tags=["users"], prefix="/users")
