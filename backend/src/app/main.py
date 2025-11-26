from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.db import Base, engine
from .models import *

from .routers import api_router, player_router


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_router.router)
app.include_router(api_router.router)


