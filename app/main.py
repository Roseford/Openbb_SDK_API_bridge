from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from . import models
from .database import engine
from app.routers import crypto
from app.routers import stocks
from app.routers import news
from app.routers import forex
from app.routers import users
from app.routers import auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(news.router)
app.include_router(crypto.router)
app.include_router(stocks.router)
app.include_router(forex.router)


models.Base.metadata.create_all(bind=engine)

