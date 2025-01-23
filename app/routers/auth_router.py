from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from app.user_manager import get_user_manager
from app.auth import auth_backend
from app.schemas.user_schemas import UserRead, UserCreate
from app.models import User
from app.oauth import github_oauth

router = APIRouter()

fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [auth_backend],
    UserRead,
    UserCreate,
)

# JWT Аутентификация
router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])

# Регистрация (встроенная в FastAPI-Users)
router.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])

# Данные о пользователе
router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

# GitHub OAuth
router.include_router(github_oauth.get_oauth_router(auth_backend, fastapi_users.get_user_manager), prefix="/auth/github", tags=["auth"])