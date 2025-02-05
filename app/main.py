from .db import init_db

from typing import Union
from datetime import date
import requests
from fastapi import FastAPI, Query
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db() 
    yield 

app = FastAPI(lifespan=lifespan)
