from fastapi_users import BaseUserManager, UUIDIDMixin
from app.models import User
from app.database import get_db
import uuid
import os
from fastapi import Depends

SECRET_KEY = os.getenv("SECRET_KEY")

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    user_db_model = User
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

async def get_user_manager(user_db=Depends(get_db)):
    yield UserManager(user_db)