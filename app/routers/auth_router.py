from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.auth_service import AuthService
from app.auth import verify_token
from app.schemas import user
from app.models import User
from sqlalchemy.future import select

router = APIRouter()

@router.post("/register", tags=["auth"])
async def register(user_data: user.UserCreate, db: AsyncSession = Depends(get_db)):
    user = await AuthService.register_user(user_data.name, user_data.email, user_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    return {"message": "Пользователь зарегистрирован"}

@router.post("/login", tags=["auth"])
async def login(user_data: user.UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    user = await AuthService.authenticate_user(user_data.email, user_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Неверный email или пароль")

    token = await AuthService.generate_token(user)

    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        samesite="Lax",
        secure=True
    )
    return {"message": "Вход выполнен"}

@router.get("/me", tags=["auth"])
async def get_me(request: Request, db: AsyncSession = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Не авторизован")

    token = token.replace("Bearer ", "")
    payload = await verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Недействительный токен")

    async with db.begin():
        result = await db.execute(select(User).filter(User.email == payload["sub"]))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")

    return {"id": user.id, "name": user.name, "email": user.email}

@router.post("/logout", tags=["auth"])
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Выход выполнен"}
