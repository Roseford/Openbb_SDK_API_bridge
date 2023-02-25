from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import crypto
from app.routers import stocks
from app.routers import news


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(news.router)
app.include_router(crypto.router)
app.include_router(stocks.router)

