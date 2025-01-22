from fastapi import FastAPI
from app.database import engine, Base, AsyncSessionLocal
from app.routers import auth_router

app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
@app.on_event('startup')
async def on_startup():
    await init_db()
    
app.include_router(auth_router.router, prefix="/auth")