from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.auth import create_access_token
from datetime import timedelta

class AuthService:
    @staticmethod
    async def register_user(name: str, email: str, password: str, db: AsyncSession):
        async with db.begin():
            result = await db.execute(select(User).filter(User.email == email))
            existing_user = result.scalars().first()
            if existing_user:
                return None

            user = User(name=name, email=email)
            await user.set_password(password)
            db.add(user)
            await db.commit()
            return user

    @staticmethod
    async def authenticate_user(email: str, password: str, db: AsyncSession):
        async with db.begin():
            result = await db.execute(select(User).filter(User.email == email))
            user = result.scalars().first()
            if not user or not await user.verify_password(password):
                return None

            return user

    @staticmethod
    async def generate_token(user: User):
        return await create_access_token({"sub": user.email}, timedelta(minutes=30))
