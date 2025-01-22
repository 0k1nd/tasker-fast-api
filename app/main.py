from fastapi import FastAPI
from database import engine, Base, AsyncSessionLocal


app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
@app.on_event('startup')
async def on_startup():
    await init_db()